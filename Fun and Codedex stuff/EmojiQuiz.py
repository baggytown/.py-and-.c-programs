import random

emoji_quiz_data = {
    "grinning_face": "😀",
    "beaming_face": "😁",
    "joy": "😂",
    "rofl": "🤣",
    "wink": "😉",
    "heart_eyes": "😍",
    "star_struck": "🤩",
    "thinking_face": "🤔",
    "shushing_face": "🤫",
    "exploding_head": "🤯",
    "partying_face": "🥳",
    "nerd_face": "🤓",
    "cool_face": "😎",
    "ghost": "👻",
    "alien": "👽",
    "robot": "🤖",
    "thumbs_up": "👍",
    "thumbs_down": "👎",
    "clapping_hands": "👏",
    "wave": "👋",
    "raised_hands": "🙌",
    "pray": "🙏",
    "flexed_biceps": "💪",
    "saluting_face": "🫡",
    "melting_face": "🫠",
    "heart_hands": "🫶",
    "dog": "🐶",
    "cat": "🐱",
    "lion": "🦁",
    "unicorn": "🦄",
    "monkey": "🐵",
    "gorilla": "🦍",
    "wolf": "🐺",
    "fox": "🦊",
    "panda": "🐼",
    "koala": "🐨",
    "tiger": "🐯",
    "dragon": "🐉",
    "apple": "🍎",
    "banana": "🍌",
    "pizza": "🍕",
    "burger": "🍔",
    "taco": "🌮",
    "coffee": "☕",
    "sushi": "🍣",
    "ramen": "🍜",
    "ice_cream": "🍦",
    "doughnut": "🍩",
    "cookie": "🍪",
    "beer": "🍺",
    "rocket": "🚀",
    "airplane": "✈️",
    "automobile": "🚗",
    "fire_engine": "🚒",
    "world_map": "🗺️",
    "volcano": "🌋",
    "ufo": "🛸",
    "bullet_train": "🚅",
    "soccer": "⚽",
    "basketball": "🏀",
    "trophy": "🏆",
    "video_game": "🎮",
    "guitar": "🎸",
    "palette": "🎨",
    "skateboarding": "🛹",
    "bow_and_arrow": "🏹",
    "headphones": "🎧",
    "popcorn": "🍿",
    "fire": "🔥",
    "sparkles": "✨",
    "party_popper": "🎉",
    "heart": "❤️",
    "broken_heart": "💔",
    "hundred": "💯",
    "rainbow": "🌈",
    "lightning": "⚡",
    "money_bag": "💰",
    "crown": "👑",
    "gem_stone": "💎"
}

score = 0
questions_count = 10

emoji_names = list(emoji_quiz_data.keys())
quiz_names = random.sample(emoji_names, questions_count)

print("--- EMOJI PYTHON QUIZ ---")
print(f"Answer {questions_count} questions. Type A, B, C, or D.\n")

for idx, correct_name in enumerate(quiz_names, 1):
    emoji_char = emoji_quiz_data[correct_name]
    
    wrong_pool = [name for name in emoji_names if name != correct_name]
    wrong_choices = random.sample(wrong_pool, 3)
    
    options = wrong_choices + [correct_name]
    random.shuffle(options)
    
    choices_map = {
        "A": options[0],
        "B": options[1],
        "C": options[2],
        "D": options[3]
    }
    
    print(f"Question {idx}: What is this emoji({emoji_char}):")
    print(f"  A. {choices_map['A']}")
    print(f"  B. {choices_map['B']}")
    print(f"  C. {choices_map['C']}")
    print(f"  D. {choices_map['D']}")
        
    user_answer = ""
    while user_answer not in ["A", "B", "C", "D"]:
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()
        
    if choices_map[user_answer] == correct_name:
        print("Correct!\n")
        score += 1
    else:
        print(f"Incorrect. The correct answer was {correct_name}.\n")
        
print("--- QUIZ COMPLETE ---")
print(f"Your final score: {score}/{questions_count}")
