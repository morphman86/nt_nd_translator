import argparse
from cache_manager import CacheManager
from chatgpt_query import ChatGPTQuery
from translator import Translator

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Translate between NT (Neurotypical) and ND (Neurodivergent) languages.")
    
    # Required argument for the phrase
    parser.add_argument("phrase", type=str, help="The phrase to translate.")
    
    # Optional argument for the translation direction, default is 'nt->nd'
    parser.add_argument(
        "--direction", 
        type=str, 
        choices=["nt->nd", "nd->nt"], 
        default="nt->nd", 
        help="Specify the translation direction: 'nt->nd' or 'nd->nt' (default: 'nt->nd')."
    )
    
    # Parse arguments
    args = parser.parse_args()

    # Initialize the cache manager and ChatGPT query handler
    cache_manager = CacheManager()
    chatgpt_query = ChatGPTQuery(cache_manager)
    
    # Initialize the Translator
    translator = Translator(cache_manager, chatgpt_query)
    
    # Perform the translation based on the provided direction
    if args.direction == "nt->nd":
        translation = translator.nt_to_nd(args.phrase)
        print(f"NT -> ND: {translation}")
    else:
        translation = translator.nd_to_nt(args.phrase)
        print(f"ND -> NT: {translation}")

if __name__ == "__main__":
    main()
