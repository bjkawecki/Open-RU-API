"use client";

const Search = () => {
  return (
    <div className="flex justify-center mt-10 space-y-5">
      <div className="flex flex-col space-y-2 w-full md:w-1/3">
        <h1 className="text-lg text-gray-700 ps-1">Wörterbuch durchsuchen</h1>
        <form>
          <div className="relative">
            <div className="flex absolute inset-y-0 items-center pointer-events-none start-0 ps-3">
              <svg
                className="w-4 h-4 text-gray-500"
                aria-hidden="true"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 20 20"
              >
                <path
                  stroke="currentColor"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2"
                  d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"
                />
              </svg>
            </div>
            <input
              type="search"
              id="default-search"
              className="block p-4 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 ps-10 focus:ring-blue-500 focus:border-blue-500 focus:outline-none focus:ring-1"
              placeholder="Russisch oder Deutsch"
              required
            />
            <button
              type="submit"
              className="text-white absolute end-2.5 bottom-2.5 bg-blue-500 hover:bg-blue-600 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded text-sm px-4 py-2"
            >
              Suchen
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default Search;
