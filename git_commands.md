# Simplest Fork Workflow (If You Choose to Fork):

Fork the Original Repository on GitHub:

Click the "Fork" button on the repository's GitHub page.

## Clone Your Fork Locally:

git clone https://github.com/your-username/original-repo.git

## Add the Original Repository as an Upstream Remote:

`cd original-repo`

`git remote add upstream https://github.com/huggingface/lerobot.git`

## Create a Branch for Your Changes:

`git checkout -b my-changes`

## Make Your Changes and Commit Them:

`git add .`

`git commit -m "Describe your changes"`

# Synchronize with Upstream as Needed:

## Fetch and merge updates from the original repository:

`git fetch upstream`

`git checkout main`

`git merge upstream/main`

## Update your feature branch:

`git checkout my-changes`

`git merge main`

## Push Your Changes to Your Fork (Optional):

`git push origin my-changes`