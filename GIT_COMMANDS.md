# Команды для выполнения работы по Git

Файл с готовыми исходниками не может создать удалённый GitHub/GitLab-репозиторий или Pull Request без вашего аккаунта. Команды ниже выполняются в терминале из папки `git-py-practice`. Дополнительные файлы (`calculator.py`, `student.py` и т. д.) уже подготовлены, но на первом коммите добавляйте только перечисленные базовые файлы, чтобы они не попали в main раньше соответствующих веток.

## Задание 1 — репозиторий и первый коммит

```bash
git init
git status
git add index.py config.py functions.py README.md .gitignore
git branch -M main
git commit -m "Initial Python project"
git log --oneline
```

## Задание 2 — изменения и отдельные коммиты

```bash
git diff
git add functions.py
git status
git commit -m "Add rectangle area function"
git add index.py
git commit -m "Use rectangle area in index"
git log -5 --oneline
```

## Задание 3 — восстановление изменений

Временно измените `return width * height` на `return width * height * 2`, затем:

```bash
git diff
git restore functions.py
python index.py
```

Измените README.md, затем:

```bash
git add README.md
git commit -m "Update README"
git show
```

## Задание 4 — калькулятор

```bash
git switch -c feature/calculator
git add calculator.py
git commit -m "Add calculator class"
git add test_calculator.py
git commit -m "Add calculator tests"
git commit --allow-empty -m "Finish calculator feature"
git switch main
git ls-tree -r --name-only main
git merge feature/calculator
```

## Задание 5 — студент и преподаватель

```bash
git switch -c feature/student
git add student.py
git commit -m "Add student class"
git commit --allow-empty -m "Add student description"
git switch main
git switch -c feature/teacher
git add teacher.py
git commit -m "Add teacher class"
git commit --allow-empty -m "Add teacher description"
git switch main
git log --oneline --graph --all
git merge feature/student
git merge feature/teacher
python -c "from student import Student; from teacher import Teacher; print(Student('Иван','ИС-21',4.5).describe()); print(Teacher('Пётр','Python',5).describe())"
git branch -d feature/student feature/teacher
```

## Задание 6 — конфликт слияния

Сначала в `main` создайте исходный `settings.py` (он уже есть в проекте):

```bash
git add settings.py
git commit -m "Add application settings"
git switch -c feature/config
```

В ветке `feature/config` измените app_name на `Education Portal`, затем:

```bash
git add settings.py
git commit -m "Change app name in feature config"
git switch main
```

В `main` измените app_name на `University System`, затем:

```bash
git add settings.py
git commit -m "Change app name in main"
git merge feature/config
```

Git должен показать конфликт. Откройте `settings.py`, вручную оставьте:

```python
SETTINGS = {
    "app_name": "University Portal",
    "debug": False,
}
```

Завершите:

```bash
git add settings.py
git commit -m "Resolve settings merge conflict"
python -m py_compile settings.py
```

## Задание 7 — отмена ошибочного коммита

Создайте `discount.py` с правильной функцией:

```python
def calculate_discount(price, percent):
    return price * percent / 100
```

Сделайте правильный коммит, затем намеренно измените формулу на ошибочную (например, `price + percent / 100`) и сделайте второй коммит:

```bash
git add discount.py
git commit -m "Add discount calculation"
# внесите намеренную ошибку в calculate_discount
git add discount.py
git commit -m "Introduce discount calculation bug"
git log --oneline
git show
git revert HEAD
```

Проверьте, что вернулась правильная формула. Ошибочный коммит остается в истории, потому что `git revert` создает новый коммит, отменяющий его изменения, а не переписывает историю.

## Задание 8 — Git Stash

```bash
git switch -c feature/product
```

Начните менять `product.py`, не завершайте метод и не коммитьте:

```bash
git stash push -m "unfinished product price"
git switch main
```

Сделайте небольшое изменение в README.md и отдельный коммит, затем:

```bash
git switch feature/product
git stash pop
```

Завершите `total_price`, затем:

```bash
git add product.py
git commit -m "Complete product total price"
```

## Задание 9 — GitHub или GitLab

1. Создайте на GitHub/GitLab пустой репозиторий `py-git-practice`.
2. Скопируйте HTTPS/SSH-адрес репозитория и выполните:

```bash
git remote add origin ВАШ_АДРЕС_РЕПОЗИТОРИЯ
git push -u origin main
git switch -c feature/order
git add order.py
git commit -m "Add order class"
git push -u origin feature/order
```

3. На сайте создайте Pull Request / Merge Request и выполните слияние.
4. Обновите локальную main:

```bash
git switch main
git pull origin main
```

## Задание 10 — командная разработка

```bash
git clone ВАШ_АДРЕС_РЕПОЗИТОРИЯ clone-one
git clone ВАШ_АДРЕС_РЕПОЗИТОРИЯ clone-two
```

В первом клоне создайте ветку `feature/user`, добавьте `user.py`, сделайте commit и push. Во втором клоне создайте `feature/auth`, добавьте `auth.py`, сделайте commit и push. Создайте два PR/MR, объедините изменения и в обоих клонах выполните:

```bash
git switch main
git pull origin main
git log --oneline --graph --all
```

## Раздел 8 — итоговое индивидуальное задание «Библиотека»

Готовая реализация находится в `library.py`, тесты — в `test_library.py`.

```bash
python -m unittest test_library -v
git switch -c develop
git switch -c feature/books
git add library.py
git commit -m "Add book management"
git switch develop
git merge feature/books
git switch -c feature/search
git add library.py
git commit -m "Add book search"
git switch develop
git merge feature/search
git switch -c feature/users
git add library.py
git commit -m "Add reader management"
git switch develop
git merge feature/users
git switch -c feature/loans
git add library.py
git commit -m "Add book loans and returns"
git switch develop
git merge feature/loans
git switch -c hotfix/validation
# внесите исправление проверки данных в library.py
git add library.py
git commit -m "Fix library validation"
git switch develop
git merge hotfix/validation
git tag -a v1.0.0 -m "Library version 1.0.0"
git switch main
git merge develop
git tag -a v1.0.0 -m "Library version 1.0.0"
```

Для сдачи итогового задания дополнительно доведите историю до 15 коммитов (добавляйте небольшие логически осмысленные коммиты), оформите 2 PR/MR через веб-интерфейс и сохраните граф `git log --oneline --graph --all`.
