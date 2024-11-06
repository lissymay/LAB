1. echo "Лиза Заневская"
2.  cd ~/otchet
 pwd >>  ~/2.txt
 whoami >> ~/2.txt
3. ls -lai ~ > ~/otchet/files/3.txt
4. echo "весело" > ~/4.txt
cat ~/4.txt > ~/4.md
5. chmod go-r ~/4.txtc
6. chmod a+x ~/4.md
7. mv ~/4.txt ~/otchet/files
mv ~/4.md ~/otchet/files
8. sudo chown root ~/otchet/files/4.md
9. sudo useradd test_user
 sudo mkdir /home/test_user
sudo chown test_user:test_user /home/test_user (права)
sudo chmod 700 /home/test_user
sudo usermod -s /bin/zsh test_user
sudo usermod -aG wheel test_user
10. sudo passwd test_user
11. sudo usermod -aG wheel test_user
12. cat /etc/passwd > ~/otchet/files/12.txt
13. chmod a+w ~/otchet/files/12.txt
14. su -P test_user
15. echo "Имя пользователя: $(whoami)" >> ~/otchet/files/12.txt
echo "Текущая рабочая директория: $(pwd)" >> ~/otchet/files/12.txt
16. sudo echo "Имя пользователя: $(whoami)" >> ~/otchet/files/12.txt
sudo echo "Текущая рабочая директория: $(pwd)" >> ~/otchet/files/12.txt
17. sudo su root
18. cd /home/test_user
echo "Имя пользователя: $(whoami)" >> ~/otchet/files/12.txt
echo "Текущая рабочая директория: $(pwd)" >> ~/otchet/files/12.txt
19. tail -n 2 ~/otchet/files/12.txt
20. sudo userdel -r test_user
21. find ~ -maxdepth 2 -type d -empty > ~/otchet/files/21.txt
22. sudo find / -maxdepth 3 -type f -name 'dev*' -user root > ~/otchet/files/22.txt
23. mkdir -p ~/test_find/time ~/test_find/permissions
24. cd ~/test_find/time
touch one.txt
touch two.txt
touch -a -t 202401010000 one.txt
touch -m -t 202410140000 two.txt
25. cd ~/test_find/permissions
touch cant_write.txt
touch can_execute.txt
chmod a-w cant_write.txt
chmod a+x can_execute.txt
26. find ~/test_find -type f -empty -atime +180
find ~/test_find -type f -empty -atime +180 -exec rm {} \;
27. find ~/test_find -type f -empty -perm 755
find ~/test_find -type f -empty -perm 755 -exec chmod a-x {} \;s
28. man ls > man_ls.txt
29. grep -n '^$' man_ls.txt
30. grep -n '[0-9]' man_ls.txts
31. grep "Richard M. Stallman and David MacKenzie" >> ~/otchet/files/31.txt
32. wc -l -c --files0-from=man_ls.txt
wc -l -c ~/man_ls.txt | awk '{print "Строки: "$1, "Размер: "$2/1024 " KB"}'
33. ps -u $(whoami) > ~/otchet/files/33.txt
34. - 
35. pgrep nano
36. kill [PID] 


