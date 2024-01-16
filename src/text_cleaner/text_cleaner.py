import re


class TextCleaner:
  def __init__(self) -> None:
    pass

  def remove_comments(self, text: str) -> str:
    text_without_comments = re.sub("(<!--.*?-->)", repl="", string=text, flags=re.DOTALL)
    return text_without_comments
  
  def remove_code_blocks(self, text: str) -> str:
    text_without_code_blocks = re.sub(r"```[^\S\r\n]*[a-z]*\n.*?\n```", repl="", string=text, count=0, flags=re.DOTALL)
    text_without_inline_code = re.sub(r"`[^\S\r\n]*[a-z]*\n.*?\n`", repl="", string=text_without_code_blocks, count=0, flags=re.DOTALL)
    return text_without_inline_code
  
  def remove_titles(self, text: str) -> str:
    text_without_titles = re.sub(r"#[^\S\r\n]*[a-z]*", repl="", string=text, flags=re.DOTALL)
    return text_without_titles
  
  def remove_links(self, text: str) -> str:
    text_without_links = re.sub(r'http\S+', repl="", string=text)
    return text_without_links
  
  def remove_line_wraps(self, text: str) -> str:
    text_without_line_wraps = re.sub(r'[\n\r\t]+', repl="", string=text)
    return text_without_line_wraps
