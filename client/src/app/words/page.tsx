"use client";

import { useEffect, useState } from "react";
import { Table } from "../../components/table";
import { Word } from "../types";

const Words = () => {
  const [words, setWords] = useState<Word[]>([]);

  async function fetchWords() {
    const config = {
      method: "GET",
      headers: { "content-type": "application/json" },
    };
    try {
      const Res = await fetch(`http://localhost:4000/${"words/"}`, config);
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
    <div className="flex justify-center mt-10">
      <Table words={words} />
    </div>
  );
};

export default Words;
