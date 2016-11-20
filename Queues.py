"""
@author: Abdurrahim Burak TEKIN
@date: 2016-11-20
Learning how Queues work!
"""

import threading, queue, math

class Consumer(threading.Thread):
    """
    Consumer -> threading.Thread
    prints the prime-numbers
    :inheritance threading.Thread:
    """

    def __init__(self, queue, file):
        """
        Constructor of the Consumer class.
        :param Queue queue: takes the queue as a parameter
        :param object prime_file: a file where the Consumer writes the prime numbers in
        """
        threading.Thread.__init__(self)
        self.queue = queue
        self.file = file

    def run(self):
        """
        waits till the producer gets the prime-numbers and then prints + writes in file
        :return None:
        """
        while True:
            number = self.queue.get()
            print("Prime number found! The number is %s" % (str(number)))
            self.file.write(str(number) + "\n")
            self.queue.task_done()


class Producer(threading.Thread):
    """
    Producer -> threading.Thread
    sends the prime-numbers to Consumer
    :inheritance threading.Thread:
    """

    def __init__(self, queue):
        """
        Constructor of the Producer class
        :param queue: takes the queue as a parameter
        """
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        """
        method primenumber is called
        if number = prime, then True -> puts in queue
        :return None:
        """
        number = 0
        while True:
            if self.primenumber(number):
                self.queue.put(number)
                self.queue.join()
            number += 1


    def primenumber(self, number):
        """
        Looks if the given parameter number is a prime number and returns a Boolean.
        Idea from the method came from the website http://stackoverflow.com/questions/18833759/python-prime-number-checker
        :param int number: Takes a number
        :return bool is_prime: Returns a Boolean to see if the given number is a prime number
        """
        if number % 2 == 0 and number > 2:
            return False
        for i in range(3, int(math.sqrt(number)) + 1, 2):
            if number % i == 0:
                return False
        return True

queue = queue.Queue()
file = open("files/Queues.txt", 'w')

producer = Producer(queue)
consumer = Consumer(queue, file)

producer.start()
consumer.start()

producer.join()
consumer.join()