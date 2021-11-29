# NYTimes-CrossWord-Puzzle-Solver

The purpose of the project is to find correct answers for the NY Times crossword puzzle by implementing AI. The accuracy rate is about 3/10 considering 16 test that are run at different dates and different puzzles. 

Solving a crossword puzzle is a two-step process that is generating a candidate answers list corresponding to each clue and choosing the most suitable one among them. 

In order to create a candidate answers list, the sources;
- Wordnet 
- Wikipedia 
- Word2vec 
- PyDictionary are used. 

As the second part of our project, it is needed to choose an answer among candidates. In this step, the algorithm proposed by us consists of two steps:
- Filter the words by the length of the answer
- Then implement the algorithm that uses the heuristic information is based on the number of intersections. 

--- 
In detail, the projects consists of 4 implementation steps:
1. Scraping & Parsing the Puzzle
2. Graphical User Interface (GUI)
3. Candidate Answers List Generation
4. Algorithm For Choosing The Answer

---


