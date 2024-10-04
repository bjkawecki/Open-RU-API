"use client";

import { useState, useEffect } from "react";
import api from "./api/api";

type Word = {
  id: number;
  name: string;
  name_accent: string;
  comment: string;
  usage: string;
  origin: string;
};

interface FormData {
  name: { value: string };
  name_accent: { value: string };
  comment: { value: string };
  usage: { value: string };
  origin: { value: string };
}

const App = () => {
  const [words, setWords] = useState([]);
  const [formData, setFormData] = useState({
    name: "",
    name_accent: "",
    comment: "",
    usage: "",
    origin: "",
  });

  const fetchWords = async () => {
    const response: any = await api("words/", {
      method: "GET",
      headers: { "content-type": "application/json" },
    });
    const data = await response.json();
    setWords(data);
  };

  useEffect(() => {
    fetchWords();
  }, []);

  const handleInputChange = (event: React.FormEvent<HTMLInputElement>) => {
    const target = event.currentTarget;
    const value = target.value;

    if (target === null) {
      throw new Error("target can not be null");
    }

    setFormData({
      ...formData,
      [target.name]: value,
    });
  };

  const handleFormSubmit = async (
    event: React.SyntheticEvent
  ): Promise<void> => {
    event.preventDefault();
    const target = event.target;
    if (target === null) {
      throw new Error("Target can not be null.");
    }
    const { name, name_accent, comment, usage, origin } =
      event.target as typeof event.target & FormData;

    await api("words/", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({
        name: name.value,
        name_accent: name_accent.value,
        comment: comment.value,
        usage: usage.value,
        origin: origin.value,
      }),
    });
    fetchWords();
    setFormData({
      name: "",
      name_accent: "",
      comment: "",
      usage: "",
      origin: "",
    });
  };

  return (
    <div className="min-h-screen bg-gray-100">
      <nav className="p-5 w-full bg-blue-500">
        <div>
          <a href="#" className="text-xl font-semibold text-white no-underline">
            Wörter
          </a>
        </div>
      </nav>
      <div className="flex justify-evenly mt-10 w-full">
        <form
          onSubmit={handleFormSubmit}
          className="p-5 w-1/4 bg-white rounded shadow"
        >
          <div className="flex flex-col mx-auto space-y-5 max-w-sm">
            <div className="flex flex-col space-y-0.5">
              <label htmlFor="name" className="">
                Wort:
              </label>
              <input
                type="text"
                name="name"
                id="name"
                className="p-1 rounded border border-slate-300 focus:ring-blue-500 focus:outline-none focus:border-blue-500 focus:ring-1"
                onChange={handleInputChange}
                value={formData.name}
              />
            </div>
            <div className="flex flex-col space-y-0.5 max-w-sm">
              <label htmlFor="name_accent" className="">
                Wort mit Akzent:
              </label>
              <input
                type="text"
                name="name_accent"
                id="name_accent"
                className="p-1 rounded border border-slate-300 focus:ring-blue-500 focus:outline-none focus:border-blue-500 focus:ring-1"
                onChange={handleInputChange}
                value={formData.name_accent}
              />
            </div>
            <div className="flex flex-col space-y-0.5 max-w-sm">
              <label htmlFor="comment" className="">
                Kommentar:
              </label>
              <input
                type="text"
                name="comment"
                id="comment"
                className="p-1 rounded border border-slate-300 focus:ring-blue-500 focus:outline-none focus:border-blue-500 focus:ring-1"
                onChange={handleInputChange}
                value={formData.comment}
              />
            </div>
            <div className="flex flex-col space-y-0.5 max-w-sm">
              <label htmlFor="usage" className="">
                Gebrauch:
              </label>
              <input
                type="text"
                name="usage"
                id="usage"
                className="p-1 rounded border border-slate-300 focus:ring-blue-500 focus:outline-none focus:border-blue-500 focus:ring-1"
                onChange={handleInputChange}
                value={formData.usage}
              />
            </div>
            <div className="flex flex-col space-y-0.5 max-w-sm">
              <label htmlFor="origin" className="">
                Herkunft:
              </label>
              <input
                type="text"
                name="origin"
                id="origin"
                className="p-1 rounded border border-slate-300 focus:ring-blue-500 focus:outline-none focus:border-blue-500 focus:ring-1"
                onChange={handleInputChange}
                value={formData.origin}
              />
            </div>
            <div className="flex justify-end">
              <button
                type="submit"
                className="px-3 py-2 text-white bg-blue-500 rounded hover:bg-blue-600 focus:ring-blue-200 focus:outline-none focus:ring-2"
              >
                Senden
              </button>
            </div>
          </div>
        </form>
        <div className="w-1/3">
          <table className="w-full text-sm text-left text-gray-500 rounded table-fixed rtl:text-right">
            <thead className="text-xs text-gray-700 uppercase bg-white rounded border-b">
              <tr>
                <th className="px-6 py-3">Wort</th>
                <th className="px-6 py-3">Mit Akzent</th>
                <th className="px-6 py-3">Kommentar</th>
                <th className="px-6 py-3">Gebrauch</th>
                <th className="px-6 py-3">Herkunft</th>
              </tr>
            </thead>
            <tbody>
              {words.map((word: Word) => (
                <tr key={word.id} className="bg-white border-b">
                  <td className="px-6 py-4">{word.name}</td>
                  <td className="px-6 py-4">{word.name_accent}</td>
                  <td className="px-6 py-4">{word.comment}</td>
                  <td className="px-6 py-4">{word.usage}</td>
                  <td className="px-6 py-4">{word.origin}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default App;
