import Link from "next/link";

export function Navbar() {
  return (
    <nav className="p-5 w-full font-semibold text-gray-200 bg-blue-500 shadow">
      <div className="flex justify-between">
        <Link href={"/"} className="text-xl no-underline">
          Wortschatz
        </Link>
        <div className="space-x-10">
          <Link href={"search"} className="no-underline">
            Suche
          </Link>
          <Link href={"words"} className="no-underline">
            Wörter
          </Link>
          <Link href={"upload"} className="no-underline">
            Upload
          </Link>
        </div>
      </div>
    </nav>
  );
}
