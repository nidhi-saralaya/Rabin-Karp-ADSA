# Rabin-Karp-ADSA

The project implements the Rabin-Karp algorithm, which is a string-searching algorithm that efficiently finds all occurrences of a pattern within a text. The implementation also includes a visualization of the algorithm's execution steps using Flask, a web framework for Python.

A brief description of the project implementation:

1. **Rabin-Karp Algorithm:**
   - **Algorithm Overview:** The Rabin-Karp algorithm uses hashing to efficiently check whether a substring of the text matches the given pattern.
   - **Hash Function:** A rolling hash function is used to compute hash values for overlapping windows of the text. This allows the algorithm to slide the window and update the hash efficiently.

2. **Flask Web Application:**
   - **Web Framework:** The implementation uses Flask to create a simple web application.
   - **HTML Form:** The web page features an HTML form that allows the user to input the text and pattern for the algorithm to search.
   - **Visualization:** The algorithm's execution steps and the pattern occurrences are displayed on the web page.

3. **HTML Visualization:**
   - **Pattern Occurrences:** The web page displays the indices where the pattern is found in the text.
   - **Algorithm Execution Steps:** The steps of the algorithm are visualized, showing the characters of the text and whether they match the pattern.

4. **Creative and Fun Elements:**
   - The web page styling uses Bootstrap for a clean and visually appealing design.
   - The display of pattern occurrences and algorithm steps could be further enhanced using creative visual elements such as tables or boxes.

5. **User Interaction:**
   - The user interacts with the application by entering the text and pattern in the form and clicking the "Search" button.

6. **Potential Enhancements:**
   - The project could be further improved by adding more creative visualizations, animations, or interactive elements to make the user experience more engaging.

Overall, the project combines the power of the Rabin-Karp algorithm with a web-based interface to make it accessible and visually interesting for users.
