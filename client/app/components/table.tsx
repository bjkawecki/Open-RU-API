import { Word } from "../types";

export function Table({ words }: any) {
  return (
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
  );
}
