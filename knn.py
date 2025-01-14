{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1d0e4687-aaee-4438-bf77-add3fd9613f7",
   "metadata": {},
   "outputs": [],
   "source": [
    "%matplotlib inline\n",
    "import matplotlib.pyplot as plt\n",
    "from sklearn.datasets import load_iris"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d81c0534-2e2a-4746-b085-03907e1f8de6",
   "metadata": {},
   "outputs": [],
   "source": [
    "iris=load_iris()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "2fc57d80-70cc-48ce-9d15-93d92ef5856f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "sklearn.utils._bunch.Bunch"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(iris)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "9ef86468-a3e2-4100-98b6-1922d58170d7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[5.1, 3.5, 1.4, 0.2],\n",
       "       [4.9, 3. , 1.4, 0.2],\n",
       "       [4.7, 3.2, 1.3, 0.2],\n",
       "       [4.6, 3.1, 1.5, 0.2],\n",
       "       [5. , 3.6, 1.4, 0.2],\n",
       "       [5.4, 3.9, 1.7, 0.4],\n",
       "       [4.6, 3.4, 1.4, 0.3],\n",
       "       [5. , 3.4, 1.5, 0.2],\n",
       "       [4.4, 2.9, 1.4, 0.2],\n",
       "       [4.9, 3.1, 1.5, 0.1],\n",
       "       [5.4, 3.7, 1.5, 0.2],\n",
       "       [4.8, 3.4, 1.6, 0.2],\n",
       "       [4.8, 3. , 1.4, 0.1],\n",
       "       [4.3, 3. , 1.1, 0.1],\n",
       "       [5.8, 4. , 1.2, 0.2],\n",
       "       [5.7, 4.4, 1.5, 0.4],\n",
       "       [5.4, 3.9, 1.3, 0.4],\n",
       "       [5.1, 3.5, 1.4, 0.3],\n",
       "       [5.7, 3.8, 1.7, 0.3],\n",
       "       [5.1, 3.8, 1.5, 0.3],\n",
       "       [5.4, 3.4, 1.7, 0.2],\n",
       "       [5.1, 3.7, 1.5, 0.4],\n",
       "       [4.6, 3.6, 1. , 0.2],\n",
       "       [5.1, 3.3, 1.7, 0.5],\n",
       "       [4.8, 3.4, 1.9, 0.2],\n",
       "       [5. , 3. , 1.6, 0.2],\n",
       "       [5. , 3.4, 1.6, 0.4],\n",
       "       [5.2, 3.5, 1.5, 0.2],\n",
       "       [5.2, 3.4, 1.4, 0.2],\n",
       "       [4.7, 3.2, 1.6, 0.2],\n",
       "       [4.8, 3.1, 1.6, 0.2],\n",
       "       [5.4, 3.4, 1.5, 0.4],\n",
       "       [5.2, 4.1, 1.5, 0.1],\n",
       "       [5.5, 4.2, 1.4, 0.2],\n",
       "       [4.9, 3.1, 1.5, 0.2],\n",
       "       [5. , 3.2, 1.2, 0.2],\n",
       "       [5.5, 3.5, 1.3, 0.2],\n",
       "       [4.9, 3.6, 1.4, 0.1],\n",
       "       [4.4, 3. , 1.3, 0.2],\n",
       "       [5.1, 3.4, 1.5, 0.2],\n",
       "       [5. , 3.5, 1.3, 0.3],\n",
       "       [4.5, 2.3, 1.3, 0.3],\n",
       "       [4.4, 3.2, 1.3, 0.2],\n",
       "       [5. , 3.5, 1.6, 0.6],\n",
       "       [5.1, 3.8, 1.9, 0.4],\n",
       "       [4.8, 3. , 1.4, 0.3],\n",
       "       [5.1, 3.8, 1.6, 0.2],\n",
       "       [4.6, 3.2, 1.4, 0.2],\n",
       "       [5.3, 3.7, 1.5, 0.2],\n",
       "       [5. , 3.3, 1.4, 0.2],\n",
       "       [7. , 3.2, 4.7, 1.4],\n",
       "       [6.4, 3.2, 4.5, 1.5],\n",
       "       [6.9, 3.1, 4.9, 1.5],\n",
       "       [5.5, 2.3, 4. , 1.3],\n",
       "       [6.5, 2.8, 4.6, 1.5],\n",
       "       [5.7, 2.8, 4.5, 1.3],\n",
       "       [6.3, 3.3, 4.7, 1.6],\n",
       "       [4.9, 2.4, 3.3, 1. ],\n",
       "       [6.6, 2.9, 4.6, 1.3],\n",
       "       [5.2, 2.7, 3.9, 1.4],\n",
       "       [5. , 2. , 3.5, 1. ],\n",
       "       [5.9, 3. , 4.2, 1.5],\n",
       "       [6. , 2.2, 4. , 1. ],\n",
       "       [6.1, 2.9, 4.7, 1.4],\n",
       "       [5.6, 2.9, 3.6, 1.3],\n",
       "       [6.7, 3.1, 4.4, 1.4],\n",
       "       [5.6, 3. , 4.5, 1.5],\n",
       "       [5.8, 2.7, 4.1, 1. ],\n",
       "       [6.2, 2.2, 4.5, 1.5],\n",
       "       [5.6, 2.5, 3.9, 1.1],\n",
       "       [5.9, 3.2, 4.8, 1.8],\n",
       "       [6.1, 2.8, 4. , 1.3],\n",
       "       [6.3, 2.5, 4.9, 1.5],\n",
       "       [6.1, 2.8, 4.7, 1.2],\n",
       "       [6.4, 2.9, 4.3, 1.3],\n",
       "       [6.6, 3. , 4.4, 1.4],\n",
       "       [6.8, 2.8, 4.8, 1.4],\n",
       "       [6.7, 3. , 5. , 1.7],\n",
       "       [6. , 2.9, 4.5, 1.5],\n",
       "       [5.7, 2.6, 3.5, 1. ],\n",
       "       [5.5, 2.4, 3.8, 1.1],\n",
       "       [5.5, 2.4, 3.7, 1. ],\n",
       "       [5.8, 2.7, 3.9, 1.2],\n",
       "       [6. , 2.7, 5.1, 1.6],\n",
       "       [5.4, 3. , 4.5, 1.5],\n",
       "       [6. , 3.4, 4.5, 1.6],\n",
       "       [6.7, 3.1, 4.7, 1.5],\n",
       "       [6.3, 2.3, 4.4, 1.3],\n",
       "       [5.6, 3. , 4.1, 1.3],\n",
       "       [5.5, 2.5, 4. , 1.3],\n",
       "       [5.5, 2.6, 4.4, 1.2],\n",
       "       [6.1, 3. , 4.6, 1.4],\n",
       "       [5.8, 2.6, 4. , 1.2],\n",
       "       [5. , 2.3, 3.3, 1. ],\n",
       "       [5.6, 2.7, 4.2, 1.3],\n",
       "       [5.7, 3. , 4.2, 1.2],\n",
       "       [5.7, 2.9, 4.2, 1.3],\n",
       "       [6.2, 2.9, 4.3, 1.3],\n",
       "       [5.1, 2.5, 3. , 1.1],\n",
       "       [5.7, 2.8, 4.1, 1.3],\n",
       "       [6.3, 3.3, 6. , 2.5],\n",
       "       [5.8, 2.7, 5.1, 1.9],\n",
       "       [7.1, 3. , 5.9, 2.1],\n",
       "       [6.3, 2.9, 5.6, 1.8],\n",
       "       [6.5, 3. , 5.8, 2.2],\n",
       "       [7.6, 3. , 6.6, 2.1],\n",
       "       [4.9, 2.5, 4.5, 1.7],\n",
       "       [7.3, 2.9, 6.3, 1.8],\n",
       "       [6.7, 2.5, 5.8, 1.8],\n",
       "       [7.2, 3.6, 6.1, 2.5],\n",
       "       [6.5, 3.2, 5.1, 2. ],\n",
       "       [6.4, 2.7, 5.3, 1.9],\n",
       "       [6.8, 3. , 5.5, 2.1],\n",
       "       [5.7, 2.5, 5. , 2. ],\n",
       "       [5.8, 2.8, 5.1, 2.4],\n",
       "       [6.4, 3.2, 5.3, 2.3],\n",
       "       [6.5, 3. , 5.5, 1.8],\n",
       "       [7.7, 3.8, 6.7, 2.2],\n",
       "       [7.7, 2.6, 6.9, 2.3],\n",
       "       [6. , 2.2, 5. , 1.5],\n",
       "       [6.9, 3.2, 5.7, 2.3],\n",
       "       [5.6, 2.8, 4.9, 2. ],\n",
       "       [7.7, 2.8, 6.7, 2. ],\n",
       "       [6.3, 2.7, 4.9, 1.8],\n",
       "       [6.7, 3.3, 5.7, 2.1],\n",
       "       [7.2, 3.2, 6. , 1.8],\n",
       "       [6.2, 2.8, 4.8, 1.8],\n",
       "       [6.1, 3. , 4.9, 1.8],\n",
       "       [6.4, 2.8, 5.6, 2.1],\n",
       "       [7.2, 3. , 5.8, 1.6],\n",
       "       [7.4, 2.8, 6.1, 1.9],\n",
       "       [7.9, 3.8, 6.4, 2. ],\n",
       "       [6.4, 2.8, 5.6, 2.2],\n",
       "       [6.3, 2.8, 5.1, 1.5],\n",
       "       [6.1, 2.6, 5.6, 1.4],\n",
       "       [7.7, 3. , 6.1, 2.3],\n",
       "       [6.3, 3.4, 5.6, 2.4],\n",
       "       [6.4, 3.1, 5.5, 1.8],\n",
       "       [6. , 3. , 4.8, 1.8],\n",
       "       [6.9, 3.1, 5.4, 2.1],\n",
       "       [6.7, 3.1, 5.6, 2.4],\n",
       "       [6.9, 3.1, 5.1, 2.3],\n",
       "       [5.8, 2.7, 5.1, 1.9],\n",
       "       [6.8, 3.2, 5.9, 2.3],\n",
       "       [6.7, 3.3, 5.7, 2.5],\n",
       "       [6.7, 3. , 5.2, 2.3],\n",
       "       [6.3, 2.5, 5. , 1.9],\n",
       "       [6.5, 3. , 5.2, 2. ],\n",
       "       [6.2, 3.4, 5.4, 2.3],\n",
       "       [5.9, 3. , 5.1, 1.8]])"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "iris.data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "5391ef12-d09f-449f-91a2-12736c8221da",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']\n"
     ]
    }
   ],
   "source": [
    "print(iris.feature_names)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "7830eafe-b94b-4ddc-8049-ddeec2219a47",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n",
      " 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1\n",
      " 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2\n",
      " 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2\n",
      " 2 2]\n"
     ]
    }
   ],
   "source": [
    "print(iris.target)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "1f168947-5b74-4cf5-90e7-c38e5a00d5fd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['setosa' 'versicolor' 'virginica']\n"
     ]
    }
   ],
   "source": [
    "print(iris.target_names)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "a4c55238-a5c9-4369-98da-f9d97ca7e5a9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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442tfz58+LASEBCgPPjgg8qePXuU9957T/H19VW++uord/wveKXOXPeXX35ZWbRokbJ//35l165dyuOPP64AUBYuXOiO/wWv9MQTTygrV65Ujhw5ouzcuVN58sknFUmSlCVLliiKwnvdWey97rzXnePsWTK8311D7bo76n7vlj0x8+fPBwCMGzeuzfEPPvgAN998MwCgqKgIx44daz2XmpqKH3/8EQ8++CDefPNNxMfH47XXXsNVV13lqrS9Xmeuu8lkwsMPP4zCwkL4+/ujX79++OGHH3DxxRe7Km2vd/LkSdx4440oKiqCwWBAdnY2fvrpJ0yePBkA73Vnsfe68153Dd7v7uGs+12jKKdGMBERERF5kW49sJeIiIi8F4sYIiIi8kosYoiIiMgrsYghIiIir8QihoiIiLwSixgiIiLySixiiIiIyCuxiCEiIiKvxCKGiDrt5ptvxrRp0xzWnkajwTfffNPh+fz8fGg0Gmzfvt1mO+PGjcMDDzxg9/ubTCb07t0ba9assfu1opqamtCjRw9s2bLFae9B1F2wiCEij1FUVISLLrpIOH758uXQaDSoqqpyyPsvWLAAycnJGDVqlEPas8bPzw8PP/wwHnvsMae9B1F3wSKGiDxGbGws/Pz83Pb+r7/+Om677Tanv8/06dOxatUq7N271+nvRdSVsYgh8lJfffUVsrKy4O/vj4iICEyaNAn19fWt5z/44AP07dsXer0effr0wb/+9a/Wc6cfy3z22WcYOXIk9Ho9+vXrh+XLl7fGtLS04NZbb0Vqair8/f2RkZGBV199VTg/RVEQFRWFhQsXth4bOHAgoqOjW/+8bt06+Pr6oq6uDkD7x0kbN25ETk4O9Ho9hgwZgm3btrX5fxg/fjwAICwsDBqNpnUjUQCQZRmPPvoowsPDERsbi6efftpmvlu3bsXBgwcxderUNsePHz+Oa6+9FuHh4QgMDMSQIUOwYcMGAMDTTz+NgQMH4v3330ePHj0QFBSEu+++Gy0tLXj++ecRGxuL6Oho/OMf/2jTZkREBEaOHIn//ve/6heSiDrULXexJvJ2RUVFuO666/D888/jiiuuQG1tLVatWoXT+7m+8847mD17Nt544w3k5ORg27ZtuP322xEYGIgZM2a0tvPII4/glVdeQWZmJl566SVcdtllOHLkCCIiIiDLMhITE/HFF18g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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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n5+PtWvXAgAWL16Mt956C0uXLsW9996Lffv24YMPPsD69ettPQ3qAVJQMjDpaaBwP0TZad0sqMAkSLFTdNWzO1AoVJAnPgnk79JNi26u1SVIEWOA5Kt0d3ncVFeqidvch3cIMOFxoDgNojhNt+aMXxSkmCmQghKN7xM3CwgdAnHxZ6AmR1exPHwEEDVBV+TUHnHFTgGCB+r6qM4GJA/d7LqYSZA8/OzSBxG5P5tXMl62bBn27duHf//73xg8eDAOHz6MoqIi3H777bj99tttGoezY8cOzJ49u9P2O+64A2vWrMGiRYuQnZ2NHTt26N/buXMnlixZgpMnTyI2NhaPP/44Fi9ebHWfXMmYiIio97H189vmBKe5uRmLFi3C559/DiEEVCoVtFotfv/732PNmjVQKq2c/dJDmOAQERH1Pg5PcFqdP38eaWlpkGUZY8eOxaBBg7pyGKdjgkNERNT72Pr53eXV+gYMGIDk5GQApqdoExEREfWELq2Y9cEHH2DEiBHw9vaGt7c3RowYgffff9/esRERERF1ic13cJ5++mn8/e9/x0MPPaSvPbVv3z4sWbIE2dnZeOGFF+weJBEREZEtbB6DEx4ejn/961+4+eabDbavX78eDz30kMmSCa6CY3CIiIh6H1s/v21+RKXVajF+/PhO28eNGweNRmPr4YiIiIjszuYE59Zbb8W7777bafvq1atxyy232CUoIiIiou7o0iyqDz74AD/88AMmT54MANi/fz9yc3Nx++23Y+nSpfp2b775pn2iJCIiIrKBzQnOiRMncMkllwDQrYUD6OpQRURE4MSJE/p2nDpOREREPcXmBGf79u2OiIOIiIjIbrq0Dg4RERGRK2OCQ0RERG6HCQ4RERG5HSY4RERE5HaY4BAREZHbYYJDREREbocJDhEREbkdJjhERETkdpjgEBERkdthgkNERERuhwkOERERuR0mOEREROR2mOAQERGR22GCQ0RERG6HCQ4RERG5HSY4RERE5HaY4BAREZHbYYJDREREbocJDhEREbkdJjhERETkdpjgEBERkdthgkNERERuhwkOERERuR0mOEREROR2mOAQERGR22GCQ0RERG6HCQ4RERG5HSY4RERE5HaY4BAREZHbYYJDREREbocJDhEREbkdJjhERETkdpjgEBERkdthgkNERERuR9XTARCZo5UFssrr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9sa2t1q+fDmqqqr0X7m5ud2MmIiIiFydynITxwgPD4dSqex0t6a4uLjTXZpW0dHRRturVCqEhYUZ3cfLywteXl76160JER9VERER9R6tn9vWDh3usQTH09MT48aNw9atW3Hdddfpt2/duhXXXHON0X1SU1Px3//+12DbDz/8gPHjx8PDw8OqfmtqagCAj6qIiIh6oZqaGgQFBVls16OzqL744gvcdtttWLVqFVJTU7F69Wq89957OHnyJBISErB8+XLk5+dj7dq1AHTTxEeMGIH77rsP9957L/bt24fFixdj/fr1uP76663qU5ZlXLx4EQEBAWYfhbmq6upqxMXFITc3t8/NAuur595XzxvguffFc++r5w303XO39ryFEKipqUFsbCwUCssjbHrsDg4A3HjjjSgrK8Pzzz+PgoICjBgxAt999x0SEhIAAAUFBQZr4iQlJeG7777DkiVL8PbbbyM2Nhb//Oc/rU5uAEChUKB///52PxdnCwwM7FP/AbTXV8+9r543wHPvi+feV88b6Lvnbs15W3PnplWPJjgAcP/99+P+++83+t6aNWs6bZs5cyYOHz7s4KiIiIioN+vxWVRERERE9sYEp5fx8vLCM888YzAzrK/oq+feV88b4Ln3xXPvq+cN9N1zd9R59+ggYyIiIiJH4B0cIiIicjtMcIiIiMjtMMEhIiIit8MEh4iIiNwOExwXtmLFCkiShEcffdRkmx07dkCSpE5fZ86ccV6gdvDss892Oofo6Giz++zcuRPjxo2Dt7c3kpOTsWrVKidFaz+2nre7XO9W+fn5uPXWWxEWFgZfX1+MGTMGhw4dMruPO1x3W8/bXa57YmKi0fN44IEHTO7jDtcbsP3c3eWaazQaPPXUU0hKSoKPjw+Sk5Px/PPPQ5Zls/vZ47r3+EJ/ZNyBAwewevVqjBo1yqr26enpBitARkREOCo0hxk+fDh+/PFH/WulUmmybVZWFhYsWIB7770X69atw88//4z7778fERERNq1s7QpsOe9W7nC9KyoqMHXqVMyePRvff/89IiMjcf78eQQHB5vcxx2ue1fOu1Vvv+4HDhyAVqvVvz5x4gQuv/xy/Pa3vzXa3h2udytbz71Vb7/mr7zyClatWoWPP/4Yw4cPx8GDB3HnnXciKCgIjzzyiNF97HbdBbmcmpoaMWjQILF161Yxc+ZM8cgjj5hsu337dgFAVFRUOC0+R3jmmWfE6NGjrW6/bNkyMWTIEINt9913n5g8ebKdI3MsW8/bXa63EEI8/vjjYtq0aTbt4w7XvSvn7U7Xvb1HHnlEDBgwQMiybPR9d7jeplg6d3e55ldeeaW46667DLYtXLhQ3HrrrSb3sdd15yMqF/TAAw/gyiuvxGWXXWb1PmPHjkVMTAzmzJmD7du3OzA6x8nIyEBsbCySkpJw0003ITMz02Tbffv2Ye7cuQbb5s2bh4MHD6K5udnRodqVLefdyh2u9zfffIPx48fjt7/9LSIjIzF27Fi89957Zvdxh+velfNu5Q7XvZVarca6detw1113mSx87A7X2xhrzr1Vb7/m06ZNw7Zt23D27FkAwNGjR7Fnzx4sWLDA5D72uu5McFzM559/jsOHD2PFihVWtY+JicHq1auxceNGbNq0CSkpKZgzZw527drl4Ejta9KkSVi7di22bNmC9957D4WFhZgyZQrKysqMti8sLERUVJTBtqioKGg0GpSWljojZLuw9bzd5XoDQGZmJt59910MGjQIW7ZsweLFi/Hwww9j7dq1Jvdxh+velfN2p+ve6j//+Q8qKyuxaNEik23c4XobY825u8s1f/zxx3HzzTdjyJAh8PDwwNixY/Hoo4/i5ptvNrmP3a67Tfd7yKFycnJEZGSkOHLkiH6bpUdUxlx11VXi6quvtnN0zlVbWyuioqLEG2+8YfT9QYMGiZdeeslg2549ewQAUVBQ4IwQHcLSeRvTW6+3h4eHSE1NNdj20EMPmb0N7Q7XvSvnbUxvve6t5s6dK6666iqzbdzhehtjzbkb0xuv+fr160X//v3F+vXrxbFjx8TatWtFaGioWLNmjcl97HXdeQfHhRw6dAjFxcUYN24cVCoVVCoVdu7ciX/+859QqVQGA9TMmTx5MjIyMhwcrWP5+flh5MiRJs8jOjoahYWFBtuKi4uhUqkQFhbmjBAdwtJ5G9Nbr3dMTAyGDRtmsG3o0KHIyckxuY87XPeunLcxvfW6A8CFCxfw448/4p577jHbzh2ud0fWnrsxvfGa//nPf8YTTzyBm266CSNHjsRtt92GJUuWmH1KYa/rzgTHhcyZMwfHjx/HkSNH9F/jx4/HLbfcgiNHjlg1uwYA0tLSEBMT4+BoHaupqQmnT582eR6pqanYunWrwbYffvgB48ePh4eHhzNCdAhL521Mb73eU6dORXp6usG2s2fPIiEhweQ+7nDdu3LexvTW6w4AH330ESIjI3HllVeabecO17sja8/dmN54zevr66FQGKYaSqXS7DRxu133Lt93Iqfo+IjqiSeeELfddpv+9d///nfx1VdfibNnz4oTJ06IJ554QgAQGzdu7IFou+5Pf/qT2LFjh8jMzBT79+8XV111lQgICBDZ2dlCiM7nnZmZKXx9fcWSJUvEqVOnxAcffCA8PDzEhg0beuoUusTW83aX6y2EEL/++qtQqVTixRdfFBkZGeLTTz8Vvr6+Yt26dfo27njdu3Le7nTdtVqtiI+PF48//nin99zxerdny7m7yzW/4447RL9+/cT//vc/kZWVJTZt2iTCw8PFsmXL9G0cdd2Z4Li4jgnOHXfcIWbOnKl//corr4gBAwYIb29vERISIqZNmya+/fZb5wfaTTfeeKOIiYkRHh4eIjY2VixcuFCcPHlS/37H8xZCiB07doixY8cKT09PkZiYKN59910nR919tp63u1zvVv/973/FiBEjhJeXlxgyZIhYvXq1wfvuet1tPW93uu5btmwRAER6enqn99z1erey5dzd5ZpXV1eLRx55RMTHxwtvb2+RnJwsnnzySdHU1KRv46jrLgkhhPX3e4iIiIhcH8fgEBERkdthgkNERERuhwkOERERuR0mOEREROR2mOAQERGR22GCQ0RERG6HCQ4RERG5HSY4RERE5HaY4BCRwy1atAjXXnutyffXrFmD4OBgp8VjSWJiIlauXGnzfmVlZYiMjER2drbdY2pVXFyMiIgI5OfnO6wPInfABIeI+ix7J1YrVqzA1VdfjcTERLsds6PIyEjcdttteOaZZxzWB5E7YIJDRGQHDQ0N+OCDD3DPPfc4vK8777wTn376KSoqKhzeF1FvxQSHyM1t2LABI0eOhI+PD8LCwnDZZZehrq5O//5HH32EoUOHwtvbG0OGDME777yjfy87OxuSJOHzzz/HlClT4O3tjeHDh2PHjh36NlqtFnfffTeSkpLg4+ODlJQU/OMf/+h23P/9738xbtw4eHt7Izk5Gc899xw0Go3+fUmS8P777+O6666Dr68vBg0ahG+++cbgGN988w0GDRoEHx8fzJ49Gx9//DEkSUJlZSV27NiBO++8E1VVVZAkCZIk4dlnn9XvW19fj7vu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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.scatter(iris.data[:,1],iris.data[:,2],c=iris.target, cmap=plt.cm.Paired)\n",
    "plt.xlabel(iris.feature_names[1])\n",
    "plt.ylabel(iris.feature_names[2])\n",
    "plt.show()\n",
    "\n",
    "plt.scatter(iris.data[:,0],iris.data[:,3],c=iris.target, cmap=plt.cm.Paired)\n",
    "plt.xlabel(iris.feature_names[0])\n",
    "plt.ylabel(iris.feature_names[3])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "41690c32-757f-4b9b-ac1c-0eab5312ebd7",
   "metadata": {},
   "outputs": [],
   "source": [
    "p=iris.data\n",
    "q=iris.target"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "27d9d6ca-8645-424d-ab26-18db95848de9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(150, 4)\n",
      "(150,)\n"
     ]
    }
   ],
   "source": [
    "print(p.shape)\n",
    "print(q.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "5b67aff6-854f-4c7e-9f09-89a0a0fadd46",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "p_train, p_test, q_train, q_test = train_test_split(p, q, test_size=0.2, random_state=4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "99999f61-64d0-41b5-90eb-f9257945a224",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(120, 4)\n",
      "(30, 4)\n"
     ]
    }
   ],
   "source": [
    "print(p_train.shape)\n",
    "print(p_test.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "54b164f0-b345-49c6-935e-903ae5fd3c16",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(120,)\n",
      "(30,)\n"
     ]
    }
   ],
   "source": [
    "print(q_train.shape)\n",
    "print(q_test.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "a6844626-5bba-4d93-9213-e92cd9b2a99f",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "from sklearn import metrics\n",
    "\n",
    "k_range=range(1,26)\n",
    "scores={}\n",
    "scores_list=[]\n",
    "for k in k_range:\n",
    "    knn=KNeighborsClassifier(n_neighbors=k)\n",
    "    knn.fit(p_train,q_train)\n",
    "    q_pred=knn.predict(p_test)\n",
    "    scores[k]=metrics.accuracy_score(q_test,q_pred)\n",
    "    scores_list.append(metrics.accuracy_score(q_test,q_pred))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "0619d3ed-0b78-4445-8118-7c9691988070",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1: 0.9333333333333333,\n",
       " 2: 0.9333333333333333,\n",
       " 3: 0.9666666666666667,\n",
       " 4: 0.9666666666666667,\n",
       " 5: 0.9666666666666667,\n",
       " 6: 0.9666666666666667,\n",
       " 7: 0.9666666666666667,\n",
       " 8: 0.9666666666666667,\n",
       " 9: 0.9666666666666667,\n",
       " 10: 0.9666666666666667,\n",
       " 11: 0.9666666666666667,\n",
       " 12: 0.9666666666666667,\n",
       " 13: 0.9666666666666667,\n",
       " 14: 0.9666666666666667,\n",
       " 15: 0.9666666666666667,\n",
       " 16: 0.9666666666666667,\n",
       " 17: 0.9666666666666667,\n",
       " 18: 0.9666666666666667,\n",
       " 19: 0.9666666666666667,\n",
       " 20: 0.9333333333333333,\n",
       " 21: 0.9666666666666667,\n",
       " 22: 0.9333333333333333,\n",
       " 23: 0.9666666666666667,\n",
       " 24: 0.9666666666666667,\n",
       " 25: 0.9666666666666667}"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "scores"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "798f8106-e701-453c-a312-da528e6fa6e0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x2c52eec32c0>]"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "plt.plot(k_range,scores_list)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "7ad780e5-414f-4adc-90ee-dd441b28282b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(24.847222222222214, 0.5, 'testing accuracy')"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "plt.xlabel('value of k for knn')\n",
    "plt.ylabel('testing accuracy')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "926301e7-a538-4802-97d3-144c834ce448",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAkkAAAHFCAYAAADmGm0KAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjkuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8hTgPZAAAACXBIWXMAAA9hAAAPYQGoP6dpAABqjElEQVR4nO3deXwTZf4H8E/uhF6IhbYItMUDikWBcrQgp1qsC+KqKyCrVNGfCB6I6MoqcuiKx4J4QBXYCsVdwZ+yrgeKFRHRihWEnxcLCNaitpYWoQc0SZP5/VFmmjRpmqSTTI7P+/XqSzuZzDwdmul3nuf7fB+VIAgCiIiIiMiJWukGEBEREYUiBklEREREbjBIIiIiInKDQRIRERGRGwySiIiIiNxgkERERETkBoMkIiIiIjcYJBERERG5wSCJiIiIyA0GSURhbtGiRVCpVKiurla6KQCAkpISLFq0CCdOnAjoeVatWoV169a5bC8rK4NKpXL7GhGRLxgkEZGsSkpKsHjxYsWCpJSUFHz++ef4wx/+ENDzE1Hk0yrdACIiORkMBmRnZyvdjLBgtVqhUqmg1fJPAZE77EkiikD//e9/0bt3bwwbNgxVVVUAgDFjxiAzMxNffvklRo4ciU6dOqF379544oknYLfbpfd+/PHHUKlUePXVV/HQQw+he/fuiI+Px2WXXYYDBw54PO+iRYtw//33AwDS09OhUqmgUqnw8ccfS/ts2rQJOTk5iImJQWxsLMaPH4+9e/c6HefIkSOYMmUKunfvDoPBgKSkJFx66aXYt28fACAtLQ3fffcdduzYIZ0jLS0NgPvhNnFI8rvvvsPUqVORkJCApKQk3HLLLTh58qTTuU+cOIEZM2agS5cuiI2NxR/+8AccOXIEKpUKixYt8vjzNzY24r777sOAAQOQkJCALl26ICcnB//5z39c9rXb7Xj++ecxYMAAmEwmdO7cGdnZ2Xjrrbec9vvXv/6FnJwcxMbGIjY2FgMGDMA//vEP6fW0tDTk5+e7HH/MmDEYM2aM9L3477phwwbcd999OOecc2AwGPDDDz/g2LFjmDVrFvr164fY2Fh069YN48aNw86dO12OazabsWTJEmRkZMBoNOLss8/G2LFjUVJSAgC49NJL0bdvX7ReO10QBJx33nns4aOwwscHogizY8cO/PGPf8SoUaPwr3/9C506dZJeq6ysxLRp03Dfffdh4cKF+Pe//4358+eje/fuuOmmm5yO89e//hUjRozA2rVrUVtbi7/85S+YOHEi9u/fD41G4/bct956K44fP47nn38emzdvRkpKCgCgX79+AIDHH38cDz/8MG6++WY8/PDDsFgsePrppzFy5EiUlpZK+1155ZWw2Wx46qmn0KtXL1RXV6OkpEQawvv3v/+N6667DgkJCVi1ahWA5h6k9lx77bWYPHkyZsyYgW+++Qbz588HABQWFgJoDlwmTpyI3bt3Y9GiRRg0aBA+//xzXHHFFV5de7PZjOPHj2PevHk455xzYLFY8OGHH+Kaa67Byy+/7HSN8/Pz8corr2DGjBlYsmQJ9Ho9vvrqK5SVlUn7PPLII3j00UdxzTXX4L777kNCQgK+/fZb/PTTT161x5358+cjJycHL774ItRqNbp164Zjx44BABYuXIjk5GTU19fj3//+N8aMGYNt27ZJwVZTUxPy8vKwc+dOzJkzB+PGjUNTUxN27dqF8vJyDB8+HPfccw8mTZqEbdu24bLLLpPO+9577+Hw4cN47rnn/G47UdAJRBTWFi5cKAAQjh07JmzYsEHQ6/XC3XffLdhsNqf9Ro8eLQAQvvjiC6ft/fr1E8aPHy99v337dgGAcOWVVzrt99prrwkAhM8//9xje55++mkBgPDjjz86bS8vLxe0Wq1w1113OW2vq6sTkpOTheuvv14QBEGorq4WAAgrVqzweJ4LL7xQGD16tMv2H3/8UQAgvPzyy9I28Ro99dRTTvvOmjVLMBqNgt1uFwRBEN59910BgFBQUOC039KlSwUAwsKFCz22qbWmpibBarUKM2bMEAYOHCht/+STTwQAwkMPPdTme48cOSJoNBph2rRpHs+RmpoqTJ8+3WX76NGjna6P+O86atQor9t96aWXCn/84x+l7UVFRQIAYc2aNW2+12azCb179xYmTZrktD0vL08499xzpWtNFA443EYUIf72t78hPz8fTzzxBJ599lmo1a4f7+TkZAwdOtRp20UXXeS2Z+Kqq65y2Q+A370YW7duRVNTE2666SY0NTVJX0ajEaNHj5aG5Lp06YJzzz0XTz/9NJYvX469e/c6DQd2hLufqbGxURqS3LFjBwDg+uuvd9pv6tSpXp/jf//3fzFixAjExsZCq9VCp9PhH//4B/bv3y/t89577wEA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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.title('knn testing accuracy')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "573d50f3-6706-4957-82b3-5e419bad05b2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-4 {\n",
       "  /* Definition of color scheme common for light and dark mode */\n",
       "  --sklearn-color-text: black;\n",
       "  --sklearn-color-line: gray;\n",
       "  /* Definition of color scheme for unfitted estimators */\n",
       "  --sklearn-color-unfitted-level-0: #fff5e6;\n",
       "  --sklearn-color-unfitted-level-1: #f6e4d2;\n",
       "  --sklearn-color-unfitted-level-2: #ffe0b3;\n",
       "  --sklearn-color-unfitted-level-3: chocolate;\n",
       "  /* Definition of color scheme for fitted estimators */\n",
       "  --sklearn-color-fitted-level-0: #f0f8ff;\n",
       "  --sklearn-color-fitted-level-1: #d4ebff;\n",
       "  --sklearn-color-fitted-level-2: #b3dbfd;\n",
       "  --sklearn-color-fitted-level-3: cornflowerblue;\n",
       "\n",
       "  /* Specific color for light theme */\n",
       "  --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));\n",
       "  --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, white)));\n",
       "  --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));\n",
       "  --sklearn-color-icon: #696969;\n",
       "\n",
       "  @media (prefers-color-scheme: dark) {\n",
       "    /* Redefinition of color scheme for dark theme */\n",
       "    --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));\n",
       "    --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, #111)));\n",
       "    --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));\n",
       "    --sklearn-color-icon: #878787;\n",
       "  }\n",
       "}\n",
       "\n",
       "#sk-container-id-4 {\n",
       "  color: var(--sklearn-color-text);\n",
       "}\n",
       "\n",
       "#sk-container-id-4 pre {\n",
       "  padding: 0;\n",
       "}\n",
       "\n",
       "#sk-container-id-4 input.sk-hidden--visually {\n",
       "  border: 0;\n",
       "  clip: rect(1px 1px 1px 1px);\n",
       "  clip: rect(1px, 1px, 1px, 1px);\n",
       "  height: 1px;\n",
       "  margin: -1px;\n",
       "  overflow: hidden;\n",
       "  padding: 0;\n",
       "  position: absolute;\n",
       "  width: 1px;\n",
       "}\n",
       "\n",
       "#sk-container-id-4 div.sk-dashed-wrapped {\n",
       "  border: 1px dashed var(--sklearn-color-line);\n",
       "  margin: 0 0.4em 0.5em 0.4em;\n",
       "  box-sizing: border-box;\n",
       "  padding-bottom: 0.4em;\n",
       "  background-color: var(--sklearn-color-background);\n",
       "}\n",
       "\n",
       "#sk-container-id-4 div.sk-container {\n",
       "  /* jupyter's `normalize.less` sets `[hidden] { display: none; }`\n",
       "     but bootstrap.min.css set `[hidden] { display: none !important; }`\n",
       "     so we also need the `!important` here to be able to override the\n",
       "     default hidden behavior on the sphinx rendered scikit-learn.org.\n",
       "     See: https://github.com/scikit-learn/scikit-learn/issues/21755 */\n",
       "  display: inline-block !important;\n",
       "  position: relative;\n",
       "}\n",
       "\n",
       "#sk-container-id-4 div.sk-text-repr-fallback {\n",
       "  display: none;\n",
       "}\n",
       "\n",
       "div.sk-parallel-item,\n",
       "div.sk-serial,\n",
       "div.sk-item {\n",
       "  /* draw centered vertical line to link estimators */\n",
       "  background-image: linear-gradient(var(--sklearn-color-text-on-default-background), var(--sklearn-color-text-on-default-background));\n",
       "  background-size: 2px 100%;\n",
       "  background-repeat: no-repeat;\n",
       "  background-position: center center;\n",
       "}\n",
       "\n",
       "/* Parallel-specific style estimator block */\n",
       "\n",
       "#sk-container-id-4 div.sk-parallel-item::after {\n",
       "  content: \"\";\n",
       "  width: 100%;\n",
       "  border-bottom: 2px solid var(--sklearn-color-text-on-default-background);\n",
       "  flex-grow: 1;\n",
       "}\n",
       "\n",
       "#sk-container-id-4 div.sk-parallel {\n",
       "  display: flex;\n",
       "  align-items: stretch;\n",
       "  justify-content: center;\n",
       "  background-color: var(--sklearn-color-background);\n",
       "  position: relative;\n",
       "}\n",
       "\n",
       "#sk-container-id-4 div.sk-parallel-item {\n",
       "  display: flex;\n",
       "  flex-direction: column;\n",
       "}\n",
       "\n",
       "#sk-container-id-4 div.sk-parallel-item:first-child::after {\n",
       "  align-self: flex-end;\n",
       "  width: 50%;\n",
       "}\n",
       "\n",
       "#sk-container-id-4 div.sk-parallel-item:last-child::after {\n",
       "  align-self: flex-start;\n",
       "  width: 50%;\n",
       "}\n",
       "\n",
       "#sk-container-id-4 div.sk-parallel-item:only-child::after {\n",
       "  width: 0;\n",
       "}\n",
       "\n",
       "/* Serial-specific style estimator block */\n",
       "\n",
       "#sk-container-id-4 div.sk-serial {\n",
       "  display: flex;\n",
       "  flex-direction: column;\n",
       "  align-items: center;\n",
       "  background-color: var(--sklearn-color-background);\n",
       "  padding-right: 1em;\n",
       "  padding-left: 1em;\n",
       "}\n",
       "\n",
       "\n",
       "/* Toggleable style: style used for estimator/Pipeline/ColumnTransformer box that is\n",
       "clickable and can be expanded/collapsed.\n",
       "- Pipeline and ColumnTransformer use this feature and define the default style\n",
       "- Estimators will overwrite some part of the style using the `sk-estimator` class\n",
       "*/\n",
       "\n",
       "/* Pipeline and ColumnTransformer style (default) */\n",
       "\n",
       "#sk-container-id-4 div.sk-toggleable {\n",
       "  /* Default theme specific background. It is overwritten whether we have a\n",
       "  specific estimator or a Pipeline/ColumnTransformer */\n",
       "  background-color: var(--sklearn-color-background);\n",
       "}\n",
       "\n",
       "/* Toggleable label */\n",
       "#sk-container-id-4 label.sk-toggleable__label {\n",
       "  cursor: pointer;\n",
       "  display: block;\n",
       "  width: 100%;\n",
       "  margin-bottom: 0;\n",
       "  padding: 0.5em;\n",
       "  box-sizing: border-box;\n",
       "  text-align: center;\n",
       "}\n",
       "\n",
       "#sk-container-id-4 label.sk-toggleable__label-arrow:before {\n",
       "  /* Arrow on the left of the label */\n",
       "  content: \"▸\";\n",
       "  float: left;\n",
       "  margin-right: 0.25em;\n",
       "  color: var(--sklearn-color-icon);\n",
       "}\n",
       "\n",
       "#sk-container-id-4 label.sk-toggleable__label-arrow:hover:before {\n",
       "  color: var(--sklearn-color-text);\n",
       "}\n",
       "\n",
       "/* Toggleable content - dropdown */\n",
       "\n",
       "#sk-container-id-4 div.sk-toggleable__content {\n",
       "  max-height: 0;\n",
       "  max-width: 0;\n",
       "  overflow: hidden;\n",
       "  text-align: left;\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-0);\n",
       "}\n",
       "\n",
       "#sk-container-id-4 div.sk-toggleable__content.fitted {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-0);\n",
       "}\n",
       "\n",
       "#sk-container-id-4 div.sk-toggleable__content pre {\n",
       "  margin: 0.2em;\n",
       "  border-radius: 0.25em;\n",
       "  color: var(--sklearn-color-text);\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-0);\n",
       "}\n",
       "\n",
       "#sk-container-id-4 div.sk-toggleable__content.fitted pre {\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-0);\n",
       "}\n",
       "\n",
       "#sk-container-id-4 input.sk-toggleable__control:checked~div.sk-toggleable__content {\n",
       "  /* Expand drop-down */\n",
       "  max-height: 200px;\n",
       "  max-width: 100%;\n",
       "  overflow: auto;\n",
       "}\n",
       "\n",
       "#sk-container-id-4 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {\n",
       "  content: \"▾\";\n",
       "}\n",
       "\n",
       "/* Pipeline/ColumnTransformer-specific style */\n",
       "\n",
       "#sk-container-id-4 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
       "  color: var(--sklearn-color-text);\n",
       "  background-color: var(--sklearn-color-unfitted-level-2);\n",
       "}\n",
       "\n",
       "#sk-container-id-4 div.sk-label.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
       "  background-color: var(--sklearn-color-fitted-level-2);\n",
       "}\n",
       "\n",
       "/* Estimator-specific style */\n",
       "\n",
       "/* Colorize estimator box */\n",
       "#sk-container-id-4 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-2);\n",
       "}\n",
       "\n",
       "#sk-container-id-4 div.sk-estimator.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-2);\n",
       "}\n",
       "\n",
       "#sk-container-id-4 div.sk-label label.sk-toggleable__label,\n",
       "#sk-container-id-4 div.sk-label label {\n",
       "  /* The background is the default theme color */\n",
       "  color: var(--sklearn-color-text-on-default-background);\n",
       "}\n",
       "\n",
       "/* On hover, darken the color of the background */\n",
       "#sk-container-id-4 div.sk-label:hover label.sk-toggleable__label {\n",
       "  color: var(--sklearn-color-text);\n",
       "  background-color: var(--sklearn-color-unfitted-level-2);\n",
       "}\n",
       "\n",
       "/* Label box, darken color on hover, fitted */\n",
       "#sk-container-id-4 div.sk-label.fitted:hover label.sk-toggleable__label.fitted {\n",
       "  color: var(--sklearn-color-text);\n",
       "  background-color: var(--sklearn-color-fitted-level-2);\n",
       "}\n",
       "\n",
       "/* Estimator label */\n",
       "\n",
       "#sk-container-id-4 div.sk-label label {\n",
       "  font-family: monospace;\n",
       "  font-weight: bold;\n",
       "  display: inline-block;\n",
       "  line-height: 1.2em;\n",
       "}\n",
       "\n",
       "#sk-container-id-4 div.sk-label-container {\n",
       "  text-align: center;\n",
       "}\n",
       "\n",
       "/* Estimator-specific */\n",
       "#sk-container-id-4 div.sk-estimator {\n",
       "  font-family: monospace;\n",
       "  border: 1px dotted var(--sklearn-color-border-box);\n",
       "  border-radius: 0.25em;\n",
       "  box-sizing: border-box;\n",
       "  margin-bottom: 0.5em;\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-0);\n",
       "}\n",
       "\n",
       "#sk-container-id-4 div.sk-estimator.fitted {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-0);\n",
       "}\n",
       "\n",
       "/* on hover */\n",
       "#sk-container-id-4 div.sk-estimator:hover {\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-2);\n",
       "}\n",
       "\n",
       "#sk-container-id-4 div.sk-estimator.fitted:hover {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-2);\n",
       "}\n",
       "\n",
       "/* Specification for estimator info (e.g. \"i\" and \"?\") */\n",
       "\n",
       "/* Common style for \"i\" and \"?\" */\n",
       "\n",
       ".sk-estimator-doc-link,\n",
       "a:link.sk-estimator-doc-link,\n",
       "a:visited.sk-estimator-doc-link {\n",
       "  float: right;\n",
       "  font-size: smaller;\n",
       "  line-height: 1em;\n",
       "  font-family: monospace;\n",
       "  background-color: var(--sklearn-color-background);\n",
       "  border-radius: 1em;\n",
       "  height: 1em;\n",
       "  width: 1em;\n",
       "  text-decoration: none !important;\n",
       "  margin-left: 1ex;\n",
       "  /* unfitted */\n",
       "  border: var(--sklearn-color-unfitted-level-1) 1pt solid;\n",
       "  color: var(--sklearn-color-unfitted-level-1);\n",
       "}\n",
       "\n",
       ".sk-estimator-doc-link.fitted,\n",
       "a:link.sk-estimator-doc-link.fitted,\n",
       "a:visited.sk-estimator-doc-link.fitted {\n",
       "  /* fitted */\n",
       "  border: var(--sklearn-color-fitted-level-1) 1pt solid;\n",
       "  color: var(--sklearn-color-fitted-level-1);\n",
       "}\n",
       "\n",
       "/* On hover */\n",
       "div.sk-estimator:hover .sk-estimator-doc-link:hover,\n",
       ".sk-estimator-doc-link:hover,\n",
       "div.sk-label-container:hover .sk-estimator-doc-link:hover,\n",
       ".sk-estimator-doc-link:hover {\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-3);\n",
       "  color: var(--sklearn-color-background);\n",
       "  text-decoration: none;\n",
       "}\n",
       "\n",
       "div.sk-estimator.fitted:hover .sk-estimator-doc-link.fitted:hover,\n",
       ".sk-estimator-doc-link.fitted:hover,\n",
       "div.sk-label-container:hover .sk-estimator-doc-link.fitted:hover,\n",
       ".sk-estimator-doc-link.fitted:hover {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-3);\n",
       "  color: var(--sklearn-color-background);\n",
       "  text-decoration: none;\n",
       "}\n",
       "\n",
       "/* Span, style for the box shown on hovering the info icon */\n",
       ".sk-estimator-doc-link span {\n",
       "  display: none;\n",
       "  z-index: 9999;\n",
       "  position: relative;\n",
       "  font-weight: normal;\n",
       "  right: .2ex;\n",
       "  padding: .5ex;\n",
       "  margin: .5ex;\n",
       "  width: min-content;\n",
       "  min-width: 20ex;\n",
       "  max-width: 50ex;\n",
       "  color: var(--sklearn-color-text);\n",
       "  box-shadow: 2pt 2pt 4pt #999;\n",
       "  /* unfitted */\n",
       "  background: var(--sklearn-color-unfitted-level-0);\n",
       "  border: .5pt solid var(--sklearn-color-unfitted-level-3);\n",
       "}\n",
       "\n",
       ".sk-estimator-doc-link.fitted span {\n",
       "  /* fitted */\n",
       "  background: var(--sklearn-color-fitted-level-0);\n",
       "  border: var(--sklearn-color-fitted-level-3);\n",
       "}\n",
       "\n",
       ".sk-estimator-doc-link:hover span {\n",
       "  display: block;\n",
       "}\n",
       "\n",
       "/* \"?\"-specific style due to the `<a>` HTML tag */\n",
       "\n",
       "#sk-container-id-4 a.estimator_doc_link {\n",
       "  float: right;\n",
       "  font-size: 1rem;\n",
       "  line-height: 1em;\n",
       "  font-family: monospace;\n",
       "  background-color: var(--sklearn-color-background);\n",
       "  border-radius: 1rem;\n",
       "  height: 1rem;\n",
       "  width: 1rem;\n",
       "  text-decoration: none;\n",
       "  /* unfitted */\n",
       "  color: var(--sklearn-color-unfitted-level-1);\n",
       "  border: var(--sklearn-color-unfitted-level-1) 1pt solid;\n",
       "}\n",
       "\n",
       "#sk-container-id-4 a.estimator_doc_link.fitted {\n",
       "  /* fitted */\n",
       "  border: var(--sklearn-color-fitted-level-1) 1pt solid;\n",
       "  color: var(--sklearn-color-fitted-level-1);\n",
       "}\n",
       "\n",
       "/* On hover */\n",
       "#sk-container-id-4 a.estimator_doc_link:hover {\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-3);\n",
       "  color: var(--sklearn-color-background);\n",
       "  text-decoration: none;\n",
       "}\n",
       "\n",
       "#sk-container-id-4 a.estimator_doc_link.fitted:hover {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-3);\n",
       "}\n",
       "</style><div id=\"sk-container-id-4\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>KNeighborsClassifier()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator fitted sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-4\" type=\"checkbox\" checked><label for=\"sk-estimator-id-4\" class=\"sk-toggleable__label fitted sk-toggleable__label-arrow fitted\">&nbsp;&nbsp;KNeighborsClassifier<a class=\"sk-estimator-doc-link fitted\" rel=\"noreferrer\" target=\"_blank\" href=\"https://scikit-learn.org/1.5/modules/generated/sklearn.neighbors.KNeighborsClassifier.html\">?<span>Documentation for KNeighborsClassifier</span></a><span class=\"sk-estimator-doc-link fitted\">i<span>Fitted</span></span></label><div class=\"sk-toggleable__content fitted\"><pre>KNeighborsClassifier()</pre></div> </div></div></div></div>"
      ],
      "text/plain": [
       "KNeighborsClassifier()"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "knn=KNeighborsClassifier(n_neighbors=5)\n",
    "knn.fit(p,q)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "cb9a08e6-b6cf-4d08-a7e2-f5962849f85a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "versicolor\n",
      "setosa\n"
     ]
    }
   ],
   "source": [
    "classes={0:'setosa',1:'versicolor',2:'virginica'}\n",
    "x_new=[[3,4,5,2],\n",
    "       [5,4,2,2]]\n",
    "y_predict=knn.predict(x_new)\n",
    "print(classes[y_predict[0]])\n",
    "print(classes[y_predict[1]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "cc7e49c5-2a46-4856-b74b-f7c73747df00",
   "metadata": {},
   "outputs": [],
   "source": [
    "#knn is suitable for lineraly seperable data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6c054f1e-6fdb-4482-890f-272788d58591",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
