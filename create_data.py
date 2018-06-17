from csv import DictWriter
from wake import get_defs, get_valid_pages

from config import path_to_data

indicators = [
  "{{en-proverb}}",
  "===Phrase===",
  "{{qualifier|idiomatic}}",
  "{{lb|en|idiom}}",
  "colloquial"
]

try:
    
    badchars = [";","\n",'"',"'","\r","\t", "]", "["]
  
    delimiter = "\t"
    fieldnames=["page_id", "page_title"]
    with open(path_to_data, "w") as f:
        writer = DictWriter(f, fieldnames=fieldnames, delimiter=delimiter)
        writer.writeheader()

    page_count = 0

    for page in get_valid_pages(name="enwiktionary"):
        
        page_count += 1
        
        if page_count % 1000 == 0:
            print("page_count:", page_count)
            
        page_text = page["text"]
        page_text_lowered = page_text.lower()
        if next(indicator in page_text_lowered for indicator in indicators):
          print("pagetitle:", page["title"])
          print("defs:", get_defs(page_text))

except Exception as e:
    print("[opd-data.create_data] found exception:", e)
    raise(e)