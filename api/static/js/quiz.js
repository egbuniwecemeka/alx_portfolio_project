document.addEventListener("DOMContentLoaded", () => {
    // Quiz duration is 5 minutes
    let timer = 5 * 60;
    const timerDisplay = document.getElementById("timer");
    const quizForm = document.getElementById("quiz-form");


    // Function to fetch questions dynamically
    async function fetchQuestions() {
        try {
            const response = await fetch('https://opentdb.com/api.php?amount=10&category=17&type=multiple');
            if (!response.ok) {
                throw new Error("Failed to fetch questions");
            }

            const data = await response.json();
            const questions = data.results;
            populateQuestions(questions);
        } catch (error) {
            console.error("Error fetching questions:", error);
        }
    }

    // Function to populate questions into the form
    function populateQuestions(questions) {
        questions.forEach((question, index) => {
            const questionContainer = document.createElement("div");
            questionContainer.className = "question-container";

            // Shuffle option for randomness
            const options = [
                { value: question.correct_answer, label: 'Correct' ,correct: true },
                { value: question.incorrect_answers[0], label: 'Option 1' ,correct: true },
                { value: question.incorrect_answers[1], label: 'Option 2' ,correct: true },
                { value: question.incorrect_answers[2], label: 'Option 3' ,correct: true },
            ]

            // Shuffle options
            options.sort(() => Math.random() - 0.5);

            questionContainer.innerHTML = `
                <label class="question-text">${question.question}</label><br>
            `;

            options.forEach((option, optionIndex) => {
                questionContainer.innerHTML += `
                    <div class="option">
                        <input type="radio" name="question${index}" value="${option.value}" required>
                        <label>${option.value}</label>
                    </div>
                `;
            });

            quizForm.appendChild(questionContainer);
        });
    }

    //Update the timer every second
    function updateTimer() {
        const minutes = Math.floor(timer / 60);
        const seconds = timer % 60;
        timerDisplay.textContent = `${minutes}:${seconds.toString().padStart(2, "0")}`;
        timer--;

        // If timer is zero
        if (timer < 0) {
            // Stop timer
            clearInterval(timerInterval);
            alert("Time's up! Submitting your quiz.");
            if (!quizForm.classList.contains("submitted")) {
                quizForm.classList.add("submitted");
                quizForm.submit(); 
            }
        }
    }

    // Start the timer
    const timerInterval = setInterval(updateTimer, 1000);
    updateTimer(); 

    // Fetch and populate questions on load page
    fetchQuestions()
});
