{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a number 371\n",
      "Number is Armstrong\n"
     ]
    }
   ],
   "source": [
    "n = input(\"Enter a number \")\n",
    "n = int(n)\n",
    "a = n\n",
    "s = 0\n",
    "while n!= 0:\n",
    "    r = n % 10\n",
    "    s = s + r**3\n",
    "    n= int(n/10)\n",
    "        \n",
    "if a == s :\n",
    "    print(\"Number is Armstrong\")\n",
    "else:\n",
    "    print(\"Number is not Armstrong\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
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
   "version": "3.6.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
