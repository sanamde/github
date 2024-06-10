def main():
    # Step 2: Create a Complex Data Structure
    about_me = {
        'full_name': 'Sanamdeep Singh',
        'student_id': 10333491,
        'pizza_toppings': ['PEPPERONI', 'MUSHROOM', 'ONION'],
        'movies': [
            {'title': 'dune', 'genre': 'sci-fi'},
            {'title': 'the Hangover', 'genre': 'comedy'}
        ]
    }
    
    # Step 3: Add Another Movie to the Data Structure
    about_me['movies'].append({'title': 'the Lord Of The Rings', 'genre': 'and fantasy'})
    
    # Step 4: Use a Function to Print Student Name and ID
    print_student_name_and_id(about_me)
    
    # Step 6: Use a Function to Print a Bullet List of Pizza Toppings
    print_pizza_toppings(about_me)
    
    # Step 5: Use a Function to Add Pizza Toppings to the Data Structure
    add_pizza_toppings(about_me, ('BACON', 'GREEN PEPPERS'))
    
    # Call the function again after adding toppings
    print_pizza_toppings(about_me)
    
    # Step 7: Use a Function to Print a Comma-Separated List of Movie Genres
    print_movie_genres(about_me)
    
    # Step 8: Use a Function to Print a Comma-Separated List of Movie Titles
    print_movie_titles(about_me['movies'])

def print_student_name_and_id(about_me):
    full_name = about_me['full_name']
    first_name = full_name.split()[0]
    print(f"My name is {full_name}, but you can call me Sir {first_name}.")
    print(f"My student ID is {about_me['student_id']}.")

def add_pizza_toppings(about_me, new_toppings):
    about_me['pizza_toppings'].extend(new_toppings)
    about_me['pizza_toppings'] = [topping.lower() for topping in sorted(about_me['pizza_toppings'])]

def print_pizza_toppings(about_me):
    print("My favourite pizza toppings are:")
    for topping in about_me['pizza_toppings']:
        print(f"- {topping}")

def print_movie_genres(about_me):
    genres = [movie['genre'] for movie in about_me['movies']]
    print(f"I like to watch {', '.join(genres)} movies.")

def print_movie_titles(movies):
    titles = [movie['title'].title() for movie in movies]
    print(f"Some of my favourite movies are {', '.join(titles)}!")

if __name__ == '__main__':
    main()
