import PyPDF2
import json
from tqdm import tqdm
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

model_id = "meta-llama/Llama-3.3-70B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device_map="auto",
    model_kwargs={"torch_dtype": torch.bfloat16},
)

def metin_al(pdf_yol):
    with open(pdf_yol, "rb") as f:
        okuyucu = PyPDF2.PdfReader(f)
        metinler = [sayfa.extract_text() for sayfa in okuyucu.pages]
    return metinler

def prompt_uret(pdf_yol):
    metinler = metin_al(pdf_yol)
    uretimler = {}
    for i, metin in tqdm(enumerate(metinler), total=len(metinler), desc="Sayfalar"):
        girdi = (
            "Verilen metni görsel olarak temsil edecek bir sahne oluşturmak için bir detaylı prompt yaz. "
            "Görsel metni göstermemeli, sadece metnin anlamını, tonunu ve temasını yansıtan bir atmosfer, semboller veya sahneler içermelidir.\n\n"
            f"Metin: {metin}"
        )
        yanit = pipe(girdi, max_new_tokens=256, return_full_text=False)
        uretimler[f"sayfa_{i + 1}"] = yanit[0]["generated_text"]
    with open("prompts.json", "w") as dosya:
        json.dump(uretimler, dosya, ensure_ascii=False, indent=4)
    return uretimler

pdf_yol = "kurk-mantolu-madonna_1123R85092.pdf"
sonuc = prompt_uret(pdf_yol)

with open("prompts.json", "r") as dosya:
    veri = json.load(dosya)
    print(json.dumps(veri, ensure_ascii=False, indent=4))