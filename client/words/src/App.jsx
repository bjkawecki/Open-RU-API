import React, { useState, useEffect } from "react";
import api from "./api";

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
    const response = await api("words/", {
      method: "GET",
      headers: { "content-type": "application/json" },
    });
    const data = await response.json();
    setWords(data);
    console.log(data);
  };

  useEffect(() => {
    fetchWords();
  }, []);

  const handleInputChange = (event) => {
    const value =
      event.target.type === "checkbox"
        ? event.target.checked
        : event.target.value;

    setFormData({
      ...formData,
      [event.target.name]: value,
    });
  };

  const handleFormSubmit = async (event) => {
    event.preventDefault();
    await api("words/", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({
        name: event.target.name.value,
        name_accent: event.target.name_accent.value,
        comment: event.target.comment.value,
        usage: event.target.usage.value,
        origin: event.target.origin.value,
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
    <div className="bg-gray-100 min-h-screen">
      <nav className="w-full bg-blue-500 p-5">
        <div>
          <a href="#" className="text-white text-xl no-underline font-semibold">
            Wörter
          </a>
        </div>
      </nav>
      <div className="flex justify-evenly w-full mt-10 ">
        <form
          onSubmit={handleFormSubmit}
          className="w-1/4 p-5 bg-white rounded shadow"
        >
          <div className="flex flex-col space-y-5 max-w-sm mx-auto">
            <div className="flex flex-col space-y-0.5">
              <label htmlFor="name" className="">
                Wort:
              </label>
              <input
                type="text"
                name="name"
                id="name"
                className="p-1 border border-slate-300 rounded focus:ring-blue-500 focus:outline-none focus:border-blue-500 focus:ring-1"
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
                className="p-1 border border-slate-300 rounded focus:ring-blue-500 focus:outline-none focus:border-blue-500 focus:ring-1"
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
                className="p-1 border border-slate-300 rounded focus:ring-blue-500 focus:outline-none focus:border-blue-500 focus:ring-1"
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
                className="p-1 border border-slate-300 rounded focus:ring-blue-500 focus:outline-none focus:border-blue-500 focus:ring-1"
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
                className="p-1 border border-slate-300 rounded focus:ring-blue-500 focus:outline-none focus:border-blue-500 focus:ring-1"
                onChange={handleInputChange}
                value={formData.origin}
              />
            </div>
            <div className="flex justify-end">
              <button
                type="submit"
                className="bg-blue-500 px-3 py-2 text-white hover:bg-blue-600 rounded focus:ring-blue-200 focus:outline-none focus:ring-2"
              >
                Senden
              </button>
            </div>
          </div>
        </form>
        <div className="w-1/3">
          <table className="w-full text-sm text-left rtl:text-right text-gray-500">
            <thead className="text-xs text-gray-700 uppercase bg-white border-b">
              <tr>
                <th className="px-6 py-3">Wort</th>
                <th className="px-6 py-3">Mit Akzent</th>
                <th className="px-6 py-3">Kommentar</th>
                <th className="px-6 py-3">Gebrauch</th>
                <th className="px-6 py-3">Herkunft</th>
              </tr>
            </thead>
            <tbody>
              {words.map((word) => (
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
