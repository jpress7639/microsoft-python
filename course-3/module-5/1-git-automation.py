# .gitignore - helps us choose which files Git should track and which ones it can safely ignore

# if you have libaries or packages installed locally, you might want to ignore them
# .gitignore lets you exclude these libraries, keeping your repository tidy.

# for files with sensitive information, like passwords or API keys, 
# you can also add them to .gitignore to prevent them from being tracked by Git.

# You can use the asterisk symbol * to match any string of characters
# Example: *.log would ignore all files ending with ".log".

# You can use the question mark ? to match any single character.
# temp?.txt would ignore files like "temp1.txt" or "tempA.txt"

# You can use square brackets [] to match any character within the brackets
# [abc].txt would ignore "a.txt", "b.txt", and "c.txt"

# You can use double asterisks ** to match any directory. 
# logs/** matches all files and folders recursively within the logs directory,
# whereas logs/* matches only files and directories immediately inside the logs directory

# You can even use the exclamation mark ! to make exceptions to your rules.
# If you want to ignore all .txt files except one called "important.txt", 
# you would use *.txt and then !important.txt

# Cheat sheet for streamlining collaboration with Git

# Understanding Git Collaboration: Building a Solid Foundation
# branches - enabling you to work on different features or bug fixes in 
# isolation without disrupting the main codebase.

# Git Commands: Working with Branches
# git branch <branch_name> is used to create a new branch
# git branch --set-upstream-to <remote>/<branch_name> an be used to set a specific branch as the upstream branch.

# git checkout <branch_name> allows you to switch between branches, 
# so you can focus on specific features or bug fixes without affecting other parts of the project

# git merge <branch_name> integrates the changes from a specific branch into your current branch.

# git reset  is often used to undo local commits or changes that haven’t been pushed to a remote repository.

# git stash  temporarily saves changes that you've made but aren't ready to commit yet. 

# Git Commands: Informational
# git status provides a snapshot of the current state of your repository, showing which files have been modified, added, or deleted
# git log displays a chronological list of all commits in your repository, along with their associated messages and authors.
# git diff shows the differences between two commits, branches, or files.

# Undoing mistakes with Git
# git revert <commit_hash> creates a new commit that undoes the changes made in a
# specific commit, preserving the history of your repository.

# git reset <commit_hash> can be used to undo changes in your working directory and staging area, 
# effectively rolling back to a previous commit.

# git commit --amend allows you to modify the most recent commit, enabling you to correct mistakes or add additional changes before pushing to a remote repository.

# Benefits of a remote repository 
# A remote repository is a version of your project that is hosted on the internet or another network.
# It allows multiple developers to collaborate on the same project,
# providing a centralized location for code storage, version control, and collaboration.