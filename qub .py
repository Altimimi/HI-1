""" ��������� ���������. ������ ������"""
import math
import random
import numpy as np
from math import e


class Qubit:
	def Onequb(): # ���������� ��������� ����� � ��������� ������������ 
		a=np.random.choice([0,1]); 
		b=np.random.choice([0,1]);
		if (a==0 and b==0): # 4 ������� ��� ������ ������������ �����������
			Pol11=0;
			bas=0;
			qubit=[[1,0],[1/math.sqrt(2),-1/math.sqrt(2)]];

		if (a==1 and b==0):
			Pol11=90;
			bas=0;
			qubit=[[0,1],[1/math.sqrt(2),1/math.sqrt(2)]];

		if (a==0 and b==1):
			Pol11=45;
			bas=1;
			qubit=[[1/math.sqrt(2),1/math.sqrt(2)],[1,0]];

	
		if (a==1 and b==1):
			Pol11=135;
			bas=1;
			qubit=[[-1/math.sqrt(2),1/math.sqrt(2)],[0,1]];


		print (Pol11);
		print (qubit);
		return ;



	def Onequb_2basis(Poll): # ��� �������� ������������� ����������� ���������� 1 ����� 
		Poll = int(input(' ������� �������� �����������(�����: 0, 45, 90, 135):' )); 
	# ��������,��� � ������ 
	# ������� ����� ������ ������ 1 �������� �� ���������� 4 ����� �����������
		if (Pol11==0;): 
			a=0;
			b=0
			qubit=[[1,0],[1/math.sqrt(2),-1/math.sqrt(2)]];

		if (Pol11==90;):
			a=1;
			b=0
			qubit=[[0,1],[1/math.sqrt(2),1/math.sqrt(2)]];

		if (Pol11==45):
			a=0;
			b=1
			qubit=[[1/math.sqrt(2),1/math.sqrt(2)],[1,0]];


		if (Pol11==135;):
			a=1;
			b=1
			qubit=[[-1/math.sqrt(2),1/math.sqrt(2)],[0,1]];

		else: 
			print('����������� ������� �����������');

		print (Poll);
		print (qubit);
		return Onequb_2basis;




	def Onequb_3basis(Poll): 
	# ��� �������� ������������� ����������� ���������� 1 �����. ������������� � ���� �������
		Poll = input(' ������� �������� ����������� ��� ������(�����: 0, 45, 90, 135,circle1, circle2):' ); 
		# ��������,��� � ������ 
	# ������� ����� ������ ������ 1 �������� �� ���������� 6 ����� �����������
		# circle1- �������������������, circle2- ������������������
		if (Pol11==0;): 

			qubit=[[1,0],[1/math.sqrt(2),-1/math.sqrt(2)]];

		if (Pol11==90;):

			qubit=[[0,1],[1/math.sqrt(2),1/math.sqrt(2)]];

		if (Pol11==45):

			qubit=[[1/math.sqrt(2),1/math.sqrt(2)],[1,0]];


		if (Pol11==135;):

			qubit=[[-1/math.sqrt(2),1/math.sqrt(2)],[0,1]];

		if (Pol11==circle1;):

			qubit=[[1/math.sqrt(2),j/math.sqrt(2)],[1,0]];

		if (Pol11==circle2;):

			qubit=[[-1/math.sqrt(2),j/math.sqrt(2)],[0,1]];

		else: 
			print('����������� ������� �����������');

		print (Poll);
		print (qubit);
		return Onequb_3basis;




	def phase_qubit();
	# ����� � ����� ��� COW
		a=np.random.choice([01,10,11]);
		ph=math.pi/3;
		phase=complex(0,ph);
		if (b==01):
			qubit0=[1,0];
			qubit1= [0,e**(phase)];

		if (b==10):
			qubit0=[0,e**(phase)];
			qubit1= [1,0];

		if (b==11):
			qubit0=[0,e**(phase)];
			qubit1= [0,e**(phase)];

		qubit_1=qubit0[0]*0+qubit0[1]*1;
		qubit_2=qubit1[0]*0+qubit1[1]*1;

		print (qubit_1);
		print (qubit_2);
		return phase_qubit;

	def ebit();
		H=np.random.choice([0,1]);
		G=np.random.choice([0,1]]);
		if (H==1):
			V1=0;
		if (H==0):
			V1=1;
		if (G==1):
			V2=0;
		if (G==1):
			V2=1;
		ebit=(1/math.sqrt(2))*((H+V1)+(G+V2));
		print("ebit=",1/math.sqrt(2),"(|",H,V1,">+|",G,V2,">)");







