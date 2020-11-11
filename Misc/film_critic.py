def rate_movie(movie):
    #print("Please rate the movie:", movie)
    rating = input("Please rate the movie: " + movie)
    print(movie + "; Your rating: " + rating)
    
rate_movie("The Meaning of Life")
print()

def age_predictor(name, current_age):
    print("Hello "+ name + ", you are " + str(current_age) + " years old.")
    print("Next year you will be " + str(current_age+1))
    
age_predictor("Eric", 67)
age_predictor(67, "Eric")