2. tree -L 2
3. cd /etc
4. ls /etc
5. ls -la /etc
6. mkdir ~/structure
7. cd ~/structure
for year in {2018..2023}
for mkdir -p $year/{files,pictures,.passwords}
8. cd ~/structure
for year in {2018..2023}
touch $year/files/data.md
9. cd ~/structure
for year in {2018..2023}
touch $year/pictures/picture.png
10. cd ~/structure
for year in {2018..2023}
touch $year/.passwords/.passwords.txt
11. cd ~/structure
for year in {2018..2023}
touch -a -t 202401010000 $year/files/data.md
12. cd ~/structure
for year in {2018..2023}
touch -m -t ${year}10061000 $year/.passwords/.passwords.txt
13. cp -r ~/structure/2023 ~/Downloads/2025
14. touch -m -t 202510060000 ~/Downloads/2025/.passwords/.passwords.txt
15. cp -r ~/Downloads/2025 ~/structure
16. mv ~/structure/2025 ~/structure/2024
17. mv ~/structure/2018/pictures/picture.png ~/structure/2018/pictures/image.png
  mv ~/structure/2019/pictures/picture.png ~/structure/2019/pictures/image.png
  mv ~/structure/2020/pictures/picture.png ~/structure/2020/pictures/image.png
  mv ~/structure/2021/pictures/picture.png ~/structure/2021/pictures/image.png
  mv ~/structure/2022/pictures/picture.png ~/structure/2022/pictures/image.png
  mv ~/structure/2023/pictures/picture.png ~/structure/2023/pictures/image.png
  mv ~/structure/2024/pictures/picture.png ~/structure/2024/pictures/image.png
18.mv ~/structure/2024 ~/Documents/
mv ~/structure/2018 ~/Documents/
19. rmdir ~/Documents/2024
20.rm -r  ~/Documents/2024
21. cat > ~/structure/2019/files/data.md 
22. nano ~/structure/2020/files/data.md
23. code  ~/structure/2021/files/data.md
24.cat ~/structure/2020/files/data.md > ~/structure/2022/files/data.md
25.mkdir ~/structure/soft_links
mkdir ~/structure/hard_links
26. ln -s ~/structure/2019 ~/structure/soft_links/2019
ln -s ~/structure/2020 ~/structure/soft_links/2020
ln -s ~/structure/2021 ~/structure/soft_links/2021
ln -s ~/structure/2022 ~/structure/soft_links/2022
ln -s ~/structure/2023 ~/structure/soft_links/2023
27. ln ~/structure/2020/files/data.md ~/structure/hard_links/data.md
ln ~/structure/2021/.passwords/.passwords.txt ~/structure/hard_links/.passwords.txt
28.mkdir ~/structure/archives
29. - 
30.mv ~/Downloads/image.png ~/structure/archives/
31.cd ~/structure/archives
tar -cvf image.tar image.png
tar -czvf image.tar.gz image.png
tar -cjvf image.tar.bz2 image.png
32. zip -r -e -P 1111 structure.zip structure
