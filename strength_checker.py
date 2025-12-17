import characters

try_again = True

def check_strength(password):

  password = password.strip()

  if len(password) < 8:
    return "Password too short, try again"
  

  score = 0
  feedback = []

  has_letter = False
  has_digits = False
  has_special_chars = False

  for char in password:
    if not has_letter and char in characters.letters:
      score = score + 1
      has_letter = True
    elif not has_digits and char in characters.digits:
      score = score + 1
      has_digits = True
    elif not has_special_chars and char in characters.special_chars:
      score = score + 1
      has_special_chars = True

  if not has_letter:
    feedback.append("Please add letters")
  if not has_digits:
    feedback.append("Please add digits")
  if not has_special_chars:
    feedback.append("Please add special characters")
  
  labels = {1: "Weak 🔴", 2: "Medium 🟡", 3: "Strong 🟢"}
  label = labels.get(score, "Unknown")

  bar_length = 10
  filled = int((score /3) * bar_length)
  strength_bar = "[" + "#" * filled + "-" * (bar_length - filled) + "]"
  percentage = int((score / 3) * 100)

  result = f"Password strength: {label} {strength_bar} ({percentage}%)"
  if feedback:
    result += "\nSuggestions:\n- " + "\n- ".join(feedback)

  return result

while try_again:
  user_input = input("Please input your password: ")
  print(check_strength(user_input))

  again = input("Want to try another password again? (Y/N) ").strip().lower()

  if again != "y":
    try_again = False
  


