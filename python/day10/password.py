password = "AI2026ML"

if len(password)>=8 and any(ch.isdigit() for ch in password):
    print("strong password")
else:
    print("wrong password")