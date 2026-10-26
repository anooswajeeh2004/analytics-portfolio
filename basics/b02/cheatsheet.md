git config --global user.name "Anas Wajeeh"
git config --global user.email "anooswork2004@gmail.com"
git config --global init.defaultBranch main

git add .gitignore basics
git status

git commit -m "Add B1 work"
git log --oneline

git status
git diff

git add basics/b01/hello.py
git commit -m "Change the greeting in hello.py"
git log --oneline

git status
git restore basics/b01/hello.py

**Sometimes you see a strange screen full of `~` lines after a Git command.** This means you are inside a text editor. Its name is Vim. Press **Esc**. Type `:q!`. Press **Enter**. To stop this, always give your commits a message with `-m`.

git remote add origin https://github.com/anooswajeeh2004/analytics-portfolio.git
git push -u origin main

git add README.md
git commit -m "Add README with data instructions"
git push

cd ~/projects
git clone https://github.com/anooswajeeh2004/analytics-portfolio.git portfolio-check
ls -a portfolio-check

one mistake:
I have problrm with athurazation in git have and i fix it
