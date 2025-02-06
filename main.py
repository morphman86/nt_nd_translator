import argparse
from cache_manager import CacheManager
from chatgpt_query import ChatGPTQuery
from translator import Translator

def main():
    parser = argparse.ArgumentParser(description="Translate between NT (Neurotypical) and ND (Neurodivergent) languages.")
    parser.add_argument("phrase", type=str, help="The phrase to translate.")
    parser.add_argument("--direction", type=str, choices=["nt->nd", "nd->nt"], default="nt->nd", help="Translation direction (default: 'nt->nd').")
    
    args = parser.parse_args()

    translator = Translator(CacheManager(), ChatGPTQuery(CacheManager()))
    translation = translator.nt_to_nd(args.phrase) if args.direction == "nt->nd" else translator.nd_to_nt(args.phrase)
    
    print(f"{args.direction.upper()}: {translation}")

if __name__ == "__main__":
    main()
