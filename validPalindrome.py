s = "A man, a plan, a canal: Panama"
clean_str = "".join([x.lower() if x.isalnum() else "" for x in s])

