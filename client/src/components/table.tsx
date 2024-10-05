import Link from "next/link";
import { Word } from "../app/types";

export function Table({ words }: any) {
  return (
    <div className="w-1/2 text-gray-500">
      <table className="w-full text-sm text-left  rounded table-fixed rtl:text-right">
        <thead className="text-xs text-gray-700 uppercase bg-white rounded border-b">
          <tr>
            <th className="p-5">Wort</th>
            <th className="p-5">Mit Akzent</th>
            <th className="p-5">Kommentar</th>
            <th className="p-5">Gebrauch</th>
            <th className="p-5">Herkunft</th>
            <th className="p-5">Details</th>
          </tr>
        </thead>
        <tbody>
          {words.map((word: Word) => (
            <tr key={word.id} className="bg-white border-b">
              <td className="p-5">{word.name}</td>
              <td className="p-5">{word.name_accent}</td>
              <td className="p-5">{word.comment}</td>
              <td className="p-5">{word.usage}</td>
              <td className="p-5">{word.origin}</td>
              <td className="p-5">
                <Link
                  href={`/words/${word.id}`}
                  key={word.id}
                  className="px-2 py-1 bg-blue-500 rounded text-white"
                >
                  Details
                </Link>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
