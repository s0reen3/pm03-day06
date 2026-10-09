# Совместное изменение регламента
Исходные значения находятся в config.txt. Ветки docs/early и docs/late создаются от одной исходной ветки lab-base. Каждая меняет одну и ту же строку независимо.

```sh
python check_config.py
```
После объединения двух требований:
```sh
python check_config.py --combined
```
Сценарии и объяснение решения фиксируйте в docs/conflict-report.md.
