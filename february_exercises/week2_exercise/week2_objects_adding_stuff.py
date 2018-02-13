class Person:
  #setting friends to none so you don't have to go back and change
  #all objects. Now may append friends.
  def __init__(self, name, email, phone, friends=None):
    self.name = name
    self.email = email
    self.phone = phone
    #statement initializes friends even if no friends added
    if friends is None:
        self.friends = []
    else:
        self.friends = friends
  #tells Python how you want things to look when you print this
  def __str__ (self):
      return self.name + '-' + self.email

  def greet(self, other_person):
    print('Hello {}, I am {}!'.format(other_person.name, self.name))
  def print_contact_info (self):
    print(self.name, self.email, self.phone)
    #Must add below statement if have a list within attribute friends
    for f in self.friends:
        print(f)

sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948', [])
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456', [])

sonny.greet(jordan)
jordan.greet(sonny)
print(sonny.email, sonny.phone)
print(jordan.name, jordan.email, jordan.phone)

sonny.print_contact_info()

#Add an instance variable(attribute) of friends

jordan.friends.append(sonny)
sonny.friends.append(jordan)
print(jordan.friends)
jordan.print_contact_info()
#Number of friends
print(len(jordan.friends))


