"use client";

import { useState, useEffect } from "react";
import { Word } from "./types";
import { Table } from "./components/table";
import { Navbar } from "./components/navbar";
import { Form } from "./components/form";

const App = () => {
  const [words, setWords] = useState<Word[]>([]);

  async function fetchWords() {
    const config = {
      method: "GET",
      headers: { "content-type": "application/json" },
    };
    try {
      const Res = await fetch(`http://localhost:3001/${"words/"}`, config);
      const words: Word[] = await Res.json();
      setWords(words);
    } catch (error) {
      console.error("Error:", error);
      return error;
    }
  }

  useEffect(() => {
    fetchWords();
  }, []);

  return (
    <div className="min-h-screen bg-gray-100">
      <Navbar />
      <div className="flex justify-evenly mt-10 w-full">
        <Form fetchWords={fetchWords} />
        <Table words={words} />
      </div>
    </div>
  );
};

export default App;
