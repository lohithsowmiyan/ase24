Tests:
Before running the experiment i have added tests in the test.py file, we can run it using the command python3 -m unittest test.py to find all the checks are working perfectly.

Extension:
To run the code add the hw3() funciton from the experiment.py under the class eg(): in ezr.py and use the command "python3 ./ezr.py -e hw3 to run it as an extension.

Inorder to verify the hypothesis:
"JJR1: Nothing works better than 50 random guessed for low dimensional problems (less than 6 x attributes)."
"JJR2: But such random guessing is rubbish for higher dimensional data. Let us test that."

firt we need to find the datasets that are low and high dimensional to run seperate experiments. So using the extend.py in ezr i found out the meta data of the datasets.

<img width="568" alt="Screenshot 2024-09-17 at 1 16 26 AM" src="https://github.com/user-attachments/assets/2aa79da9-6a17-41cd-9e21-2bf828956f11">

Inorder to verify "JJR1" i used this snippet in the Makefile which have the manually added lo dimensional datasets 

<img width="1027" alt="Screenshot 2024-09-17 at 1 06 45 AM" src="https://github.com/user-attachments/assets/021565e0-10d2-4da8-859d-e435adbee3ba">

after running rq.sh in ~tmp/hw3_lo folder i got these results..

<img width="999" alt="Screenshot 2024-09-17 at 1 06 22 AM" src="https://github.com/user-attachments/assets/d5b6730c-fd51-4f0a-903c-bb807091e7eb">

After seeing that Random treatment appeared 73% of the times under ranking 0 which is a close 2nd best after exploit/b=True it seems that we can confirm Random works very well for lo dimensional datasets however it did not outperform exploit/b=True.

Inorder to verify "JJRR" i used this snippet in the Makefile which have the manually added hi dimensional datasets 

<img width="1005" alt="Screenshot 2024-09-17 at 1 24 56 AM" src="https://github.com/user-attachments/assets/0cb2348a-e439-4cb6-bd81-99b08f8203f6">

after running rq.sh in ~tmp/hw3_hi folder i got these results..

<img width="876" alt="Screenshot 2024-09-17 at 2 11 33 AM" src="https://github.com/user-attachments/assets/93f85b75-5580-433e-85d1-9d5ce7781b4e">

After seeing that Random treatment appeared 56% of the times under ranking 0 which is significantly lower compared to explore/b=False and exploit/b=True both of which ranked 83% under rank 0 it seems that we can confirm Random works very well for lo dimensional however it does not work as well in hi dimensional datasets.









