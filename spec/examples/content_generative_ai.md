# Content Source: Generative AI Fundamentals

This file demonstrates the Content Source format for TDL.
Sections are referenced by learning units via `source_sections`.

---

## Section: Foundation Models

Foundation Models are large-scale neural networks pre-trained on vast amounts of diverse data. They represent a paradigm shift in AI development: instead of training specialized models for each task, we train a single large model that can be adapted to many downstream applications.

Key characteristics of Foundation Models:

1. **Scale**: Trained on billions of parameters and terabytes of data
2. **Generality**: Can perform many tasks without task-specific training
3. **Transferability**: Knowledge transfers to new domains via fine-tuning
4. **Emergence**: Capabilities that appear only at sufficient scale

Examples include GPT-4 (OpenAI), Claude (Anthropic), LLaMA (Meta), and PaLM (Google).

The term "Foundation Model" was coined by Stanford researchers in 2021 to emphasize that these models serve as a foundation upon which many applications are built.

---

## Section: Transformer Architecture

The Transformer architecture was introduced in the 2017 paper "Attention Is All You Need" by Vaswani et al. It revolutionized natural language processing by replacing recurrent neural networks (RNNs) with a purely attention-based mechanism.

Key innovations:

1. **Self-Attention**: Each position can attend to all positions in the input
2. **Parallelization**: Unlike RNNs, transformers process all positions simultaneously
3. **Positional Encoding**: Since there's no inherent sequence processing, position information is added explicitly

Architecture components:
- Encoder: Processes input sequence
- Decoder: Generates output sequence
- Multi-Head Attention: Multiple attention mechanisms in parallel
- Feed-Forward Networks: Position-wise fully connected layers

The Transformer's efficiency and effectiveness made it the foundation for all major language models today.

---

## Section: Attention Mechanism

The attention mechanism allows a model to focus on relevant parts of the input when producing each part of the output. It answers the question: "Which input elements are most relevant for producing this output element?"

Mathematical intuition (simplified):
- Query (Q): What am I looking for?
- Key (K): What do I have to offer?
- Value (V): What information do I provide?

Attention(Q, K, V) = softmax(QK^T / √d) × V

Types of attention:
1. **Self-attention**: Sequence attends to itself
2. **Cross-attention**: One sequence attends to another
3. **Multi-head attention**: Multiple attention patterns in parallel

The Felix example illustrates why attention matters:
"Felix saw a black cat and a white cat. He gave food to it."

To understand what "it" refers to, the model must attend to earlier parts of the sentence. Attention provides this mechanism.

---

## Section: Prompting Techniques

Effective prompting is crucial for getting useful outputs from generative AI. Key techniques include:

**1. Zero-shot prompting**
Simply state what you want without examples.
Example: "Translate the following English text to French: Hello, how are you?"

**2. Few-shot prompting**
Provide examples of the desired input-output pattern.
Example:
"Translate English to French:
English: Hello -> French: Bonjour
English: Goodbye -> French: Au revoir
English: Thank you -> French:"

**3. Chain-of-thought prompting**
Ask the model to show its reasoning step by step.
Example: "Solve this problem step by step: If a train travels 60 mph for 2.5 hours..."

**4. System prompts**
Set the context and behavior for the entire conversation.
Example: "You are a helpful coding assistant. Always explain your code clearly."

**5. Structured output**
Specify the exact format you want.
Example: "Return your answer as JSON with keys: 'summary', 'key_points', 'conclusion'"
