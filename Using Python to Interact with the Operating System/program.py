def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open( "program.py", "w")as f:
    filesize =  f.write(comments)
  return(filesize)

print(create_python_script("program.py"))
