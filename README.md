# 🚀 SEO-Optimized Article Generator using CrewAI

An AI-powered multi-agent system that automatically generates **high-quality, SEO-optimized articles** using **CrewAI**. This project simulates a real-world content production pipeline with specialized agents for research, planning, writing, and optimization.

---

## 📌 Overview

The **SEO Article Generator** leverages multiple AI agents collaborating together to produce structured, engaging, and search-engine-friendly content from a simple user input (topic or keyword).

Instead of a single model handling everything, this system distributes tasks across agents—making the workflow modular, scalable, and efficient.

---

## ✨ Features

- 🔍 **Keyword Research Agent**
  - Finds high-ranking and relevant SEO keywords

- 🧠 **Content Strategist Agent**
  - Creates structured outlines (H1, H2, H3)

- ✍️ **Content Writer Agent**
  - Generates high-quality, human-like articles

- 📈 **SEO Optimization Agent**
  - Improves keyword density, readability, and metadata

- 🔄 **Multi-Agent Collaboration**
  - Agents work sequentially using CrewAI workflows

---

## 🛠️ Tech Stack

- Python  
- CrewAI  
- LLMs (OpenAI / Gemini / others)  
- YAML / JSON (for agent configs)  
- dotenv (.env) for API key management  

---

## ⚙️ Project Structure

```
seo-article-generator/
│── agents/
│   ├── keyword_agent.py
│   ├── strategist_agent.py
│   ├── writer_agent.py
│   └── seo_agent.py
│
│── tasks/
│   └── tasks.yaml
│
│── crew.py
│── main.py
│── requirements.txt
│── .env
│── README.md
```

---

## 🔄 Workflow

1. User inputs a topic/keyword  
2. Keyword Agent → finds SEO keywords  
3. Strategist Agent → builds article outline  
4. Writer Agent → generates article  
5. SEO Agent → optimizes content  
6. Output → ready-to-publish SEO article  

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/seo-article-generator.git
cd seo-article-generator
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup environment variables

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_api_key_here
```

---

### 4. Run the project

```bash
python main.py
```

---

## 📊 Example Input

```
Enter Topic: "Benefits of Artificial Intelligence in Healthcare"
```

---

## 📄 Example Output

- SEO-friendly title  
- Structured headings  
- Keyword-rich content  
- Meta description  

---

## 🎯 Use Cases

- Blogging platforms  
- Content automation tools  
- Digital marketing agencies  
- Affiliate marketing  
- Startup content pipelines  

---

## 📈 Advantages

- Saves time  
- Scalable content generation  
- SEO best practices  
- Modular architecture  

---

## 🔮 Future Improvements

- CMS integration (WordPress, Webflow)  
- Multilingual content generation  
- Real-time SEO scoring  
- Plagiarism detection  
- AI image generation  

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository  
2. Create your feature branch (`git checkout -b feature-name`)  
3. Commit your changes (`git commit -m 'Add feature'`)  
4. Push to the branch (`git push origin feature-name`)  
5. Open a Pull Request  

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Dipanshu Agrawal**

---

## ⭐ Support

If you like this project, please consider giving it a ⭐ on GitHub!
