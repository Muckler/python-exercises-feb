class Person:
  #setting friends to none so you don't have to go back and change
  #all objects. Now may append friends.
  def __init__(self, name, email, phone, friends=None, greeting_count=0):
    self.name = name
    self.email = email
    self.phone = phone
    self.greeting_count = greeting_count
    #statement initializes friends even if no friends added
    if friends is None:
        self.friends = []
    else:
        self.friends = friends
  #tells Python how you want things to look when you print this
  def __str__ (self):
      return self.name + '-' + self.email

  def greet(self, other_person):
    #counter to know how many times greeting method called
    self.greeting_count += 1
    print('Hello {}, I am {}!'.format(other_person.name, self.name))
  #add_friend module create parameter friend which is beeing passed
  #when method is called
  def add_friend(self, friend):
      #adding the parameter friend to attribute friends and adding to 
      #list of friends
      self.friends.append(friend)
  def num_friends(self):
      print(len(self.friends))
  
  def print_contact_info (self):
    print(self.name, self.email, self.phone)
    #Must add below statement if have a list within attribute friends
    for f in self.friends:
        print(f.name)

sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948', [])
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456', [])

sonny.greet(jordan)
jordan.greet(sonny)
print(sonny.email, sonny.phone)
print(jordan.name, jordan.email, jordan.phone)

sonny.print_contact_info()

#Call method add_friends to add Jordan as friend
sonny.add_friend(jordan)
#specify first item of list friends and print attribute name
print(sonny.friends[0].name)

#Number of friends
print(jordan.num_friends())
print(sonny.greeting_count)
sonny.greet(jordan)
print(sonny.greeting_count)
sonny.greet(jordan)
print(sonny.greeting_count)



