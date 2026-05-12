import sys
from pipeline.string_vectorizer import process_string_to_vector

def main():
    success = process_string_to_vector("Hello, this is a test string to be vectorized.")
    if success:
        print("Successfully vectorized and stored.")
        sys.exit(0)
    else:
        print("Failed to vectorize.")
        sys.exit(1)

if __name__ == "__main__":
    main()
