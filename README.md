# airus-proj2
a Bash command-line tool that performs a useful data preparation task

* Clone repo into Cloud9 (pick a machine with decent size CPU and RAM if possible, but students should use micro)
* Add ssh keys to GitHub
* [resize to bigger disk](https://gist.github.com/wongcyrus/a4e726b961260395efa7811cab0b4516)
* Create virtualenv and add to bashrc and source
`python3 -m venv ~/.venv && echo 'source ~/.venv/bin/activate' >> ~/.bashrc && source ~/.bashrc`
* cd into checkout and run `make install`
* Preview running command_line_tool app after running:  python app.py describe
* create a new ECR registry and follow the push command
* Navigate to ECR repo created <cdfastapi> or whatever you named it and follow "push" instructions
  
  <img width="1835" alt="Screen Shot 2022-09-28 at 12 36 45 PM" src="https://user-images.githubusercontent.com/58792/192838151-ca89bdc1-bb99-40dc-ace1-f059e07ba5f6.png">

* verify it runs in a new cloud9 instance: docker run -it 954946645007.dkr.ecr.us-east-1.amazonaws.com/command:latest python app.py describe