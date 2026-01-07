import random
import datetime
from fuzzywuzzy import process
from knowledge_base import IOCL_DATA, FAQ_PATTERNS

class IOCLBot:
    def __init__(self):
        # Flatten patterns for fuzzy matching
        self.intent_map = {}
        for item in FAQ_PATTERNS:
            for pattern in item['patterns']:
                self.intent_map[pattern] = item['intent']

    def get_response(self, user_text):
        user_text = user_text.lower().strip()
        
        # 1. Direct Keyword / Fuzzy Matching
        all_patterns = list(self.intent_map.keys())
        best_match, score = process.extractOne(user_text, all_patterns)
        
        if score > 70:  # Threshold for fuzzy matching
            intent = self.intent_map[best_match]
            for item in FAQ_PATTERNS:
                if item['intent'] == intent:
                    return random.choice(item['responses'])

        # 2. Logic-based domain search
        if "headquarters" in user_text or "office" in user_text:
            return IOCL_DATA['company_info']['headquarters']
        
        if "chairman" in user_text or "head" in user_text:
            return IOCL_DATA['company_info']['leadership']

        # 3. Fallback
        return "I'm sorry, I couldn't find specific info on that. You can try asking about 'LPG booking', 'XP95 petrol', or 'IOCL careers'. Or call our toll-free number: 1800-233-3555."

def get_bot_response(message):
    bot = IOCLBot()
    response = bot.get_response(message)
    return {
        "response": response,
        "timestamp": datetime.datetime.now().isoformat()
    }