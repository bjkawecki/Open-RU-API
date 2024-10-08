"use client";

import { useState, useEffect } from "react";
import { Word } from "./types";
import { Table } from "../components/table";

const App = () => {
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
    <div className="">
      <div className="flex justify-evenly mt-10 w-full">
        {/* <pre>{JSON.stringify(words, null, 2)}</pre> */}
        <Table words={words} />
      </div>
    </div>
  );
};

export default App;
