""" Kahoot """

def main():
  # imports
  import json
  
  # score
  score = 0
  
  def precent():
    return (score / len(answers.keys())) * 100
  
  
  # banner
  banner = """
   █████   ████           █████                         █████   
  ░░███   ███░           ░░███                         ░░███    
   ░███  ███     ██████   ░███████    ██████   ██████  ███████  
   ░███████     ░░░░░███  ░███░░███  ███░░███ ███░░███░░░███░   
   ░███░░███     ███████  ░███ ░███ ░███ ░███░███ ░███  ░███    
   ░███ ░░███   ███░░███  ░███ ░███ ░███ ░███░███ ░███  ░███ ███
   █████ ░░████░░████████ ████ █████░░██████ ░░██████   ░░█████ 
  ░░░░░   ░░░░  ░░░░░░░░ ░░░░ ░░░░░  ░░░░░░   ░░░░░░     ░░░░░  
  """
  
  print(banner)
  
  # load file
  file = input("\n[!] enter file name: ")
  
  with open(file, "r") as f:
      data = f.read()
      data = json.loads(data)
      questions = data["questions"]
      title = data["title"]
      description = data["description"]
      author = data["author"]
      answers = data["answers"]
  
  # print data
  print(f"\n[*] Title: {title}")
  print(f"[*] Description: {description}")
  print(f"[*] Author: {author}\n")
  
  
  for i in questions:
    n = 0
    data = questions[i]
    print("\n" + data["question"] + "\n")
    
    for j in data["possible_answers"]:
      print(f"\t {n}. {j}")
      n+=1
  
    answer = input("\nenter choice: ")
  
    if data["possible_answers"][int(answer)] in answers[i]:
      score +=1
      print("\nyou got it correct")
  
    else:
      print("\nyou got it wrong")
      print(f"Correct answer: {answers[i]}")
  
  # end
  print(f"\nyour score: {score}/{len(answers.keys())} or {precent()}%")

try:
  if __name__ == "__main__":
    main()

except:
  print("ERROR")
