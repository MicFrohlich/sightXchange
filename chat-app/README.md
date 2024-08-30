# Dynamic AI-Powered Website Builder

## Project Overview

This project is a dynamic, AI-powered website builder designed to create an engaging and interactive user experience. The AI agent starts a conversation with users to understand their preferences and build a website tailored to their desires. As the user interacts with the AI, the website is dynamically constructed in the background, with aesthetic elements being added based on user input. The site can also dynamically fetch and display images (PNGs) relevant to the user's preferences, creating a visually rich and personalized experience.

## Features

- **Interactive AI Agent**: The AI initiates a conversation to learn about the user's preferences for their website, asking questions and making suggestions based on their responses.
- **Dynamic Website Construction**: The website is built in real-time as the user interacts with the AI, with elements being added based on sentiment analysis and user preferences.
- **Sentiment-Based Visuals**: The website adjusts its visual elements based on the sentiment of the conversation, using animations and images to reflect the user's mood and choices.
- **Dynamic Image Loading**: The site dynamically fetches and displays relevant images (PNGs) based on user input, using either predefined assets or images fetched from external sources.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/dynamic-website-builder.git
   cd dynamic-website-builder
   ```

2. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables**:
    - Create a .env file in the project root with your API keys:
    ```bash
        GROQ_API_KEY=your_groq_api_key_here
        UNSPLASH_ACCESS_KEY=your_unsplash_access_key_here
    ```

4. **Run the application**:
    ```bash
        python app.py
    ```

5. **Access the application**:
    - Open your browser and go to http://127.0.0.1:5000/.

## How It Works

- Initial Interaction: When the user connects to the site, the AI agent greets them and starts by asking what kind of design or elements they are looking for in their website.
- User Input Analysis: The AI analyzes the user's responses, determining their design preferences and mood using sentiment analysis.
- Dynamic Content Generation: Based on the user's input, the AI dynamically adds visual elements to the site, such as images, animations, and background colors. It also fetches relevant images dynamically from external sources.
- Ongoing Interaction: The AI continues to guide the user, asking follow-up questions and refining the website design based on ongoing input.

## Project Structure
- app.py: The main Flask application that handles server-side logic, including AI interactions and dynamic content updates.
- templates/index.html: The front-end HTML template where the chat interface and dynamic elements are rendered.
- static/style.css: The CSS file containing styles and animations for the visual elements.
- requirements.txt: Lists the Python dependencies required for the project.

## Future Enhancements

- Advanced Image Search: Integrate more advanced image search capabilities to fetch highly relevant images based on complex user queries.
- Customizable Themes: Allow users to choose from a variety of themes that can be dynamically applied to the website.
- User Accounts: Implement user accounts and save progress, allowing users to return and continue building their website.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- Groq: For providing the AI chat capabilities.
- Unsplash: For the images used in dynamic content generation.

## Contact

For any questions or issues, please contact Michael Adam Frohlich.