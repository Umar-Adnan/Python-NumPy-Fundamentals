# 🐍 Master NumPy & Building a Resizable Photo Puzzle Engine

> **A hands-on journey from core numerical computing in Python to building a full-featured, resizable desktop puzzle application using NumPy matrix manipulation and Tkinter.**

---

## 🚀 Overview

This repository documents a step-by-step learning progression in Python's **NumPy** library, transitioning from fundamental array mechanics to applying vectorization techniques in real-world projects.

The culmination of this repository is an **Interactive Photo Scrambler & Reassembler** game that treats digital photos as multi-dimensional numerical tensors ($\text{Height} \times \text{Width} \times \text{RGB Channels}$) to scramble, render, and verify visual puzzle states entirely through linear algebra and matrix operations.

---

## 📚 What Was Learned (NumPy Core Concepts)

Throughout this repository, core numerical computing concepts were mastered through structured code implementations and practical mini-projects:

### 1. Array Foundations & Creation
* **Memory & Layout:** Understanding contiguous C-contiguous memory blocks vs Python standard lists.
* **Initialization Routines:** Using `np.array`, `np.zeros`, `np.ones`, `np.arange`, `np.linspace`, and `np.random` generators.
* **Data Types (`dtypes`):** Managing memory efficiency by choosing between integer precision (`int64`, `int32`) and floating-point representations.

### 2. Array Manipulation & Reshaping
* **Dimension Transformations:** Using `.reshape()`, flattening with `.ravel()` / `.flatten()`, and transposing axes (`np.transpose`).
* **Views vs Copies:** Understanding memory sharing during reshaping operations vs explicit memory copies via `.copy()`.
* **Block Stacking:** Joining matrices along specific axes using `np.hstack` (horizontal stacking) and `np.vstack` (vertical stacking).

### 3. Vectorization & Broadcasting
* **Vectorized Math:** Replacing slow Python `for` loops with compiled C-level universal functions (`ufuncs`).
* **Broadcasting Rules:** Performing element-wise arithmetic across arrays of different shapes according to NumPy's alignment rules.
* **In-place Operations:** Modifying array buffers directly via assignment operators (`+=`, `*=`).

### 4. Handling Missing & Special Values
* **Detection:** Identifying invalid values using `np.isnan()`, `np.isinf()`, and `np.isfinite()`.
* **Imputation & Filtering:** Cleaning dirty datasets using boolean indexing and `np.where()`.
* **Preserving Structure:** Utilizing Masked Arrays (`np.ma.masked_invalid`) to isolate invalid spatial grid points while retaining strict array coordinate boundaries.

---

## 🧩 The Highlight Project: Widescreen Photo Scrambler

An interactive desktop application built using **Tkinter** and **Pillow**, powered under the hood by **NumPy matrix operations**.

### ⚡ Game Features
* 🖼️ **Custom Photo Support:** Pass any local `.jpg` or `.png` file path directly into the engine.
* 📐 **Dynamic Resizability:** Drag to resize or maximize the window—the underlying NumPy matrices scale, re-slice, and re-stack on the fly.
* ⏱️ **Preview Countdown & Live Timer:** Memorize the target image during a 3-second preview phase before scrambling.
* 🔢 **Numbered Tile Badges:** Subtly badged tiles keep gameplay intuitive and fun.
* ⚡ **Pure Matrix Operations:** All image slicing, horizontal (`np.hstack`), vertical (`np.vstack`) block-stacking, and solution validation are computed using NumPy array manipulation.

---

## 🛠️ Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
   cd your-repo-name
