import { useState } from "react";
import { FormData } from "../types";
import { api } from "../api/api";

export function Form({ fetchWords }: any) {
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
  const [formData, setFormData] = useState({
    name: "",
    name_accent: "",
    comment: "",
    usage: "",
    origin: "",
  });
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
  return (
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
  );
}
