def is_palindrome(text: str) -> bool:
     """ Это функция находит полиндрома"""
     text = text.lower()
     return text == text[::-1]



