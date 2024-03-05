# Создание SSH
ssh-keygen -t NAME -C "youremail@gmail.com"

# Добавление SSH кода в GitHub
Go to GitHub, navigate to the top left corner, click your profile, and select: Settings:
Then select "SSH and GPG keys". and click the "New SSH key" button:
Select a title, and paste the public SSH key into the "Key" field, and click "Add SSH Key":
You will be prompted to supply your GitHub password.

# Клонирование репозитория
git clone git@github.com:USERNAME/repository.git
