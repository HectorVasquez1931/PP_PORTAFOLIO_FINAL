#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os
from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any


# -------------------------
# CLASES (POO)
# -------------------------

class Item(ABC):
    def __init__(self, item_id: int, title: str, publication_year: int, quantity: int):
        self._id = int(item_id)
        self._title = str(title)
        self._publication_year = int(publication_year)
        self._quantity = int(quantity)

    # Encapsulamiento: getters/setters
    @property
    def id(self) -> int:
        return self._id

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str):
        self._title = str(value)

    @property
    def publication_year(self) -> int:
        return self._publication_year

    @publication_year.setter
    def publication_year(self, value: int):
        self._publication_year = int(value)

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, value: int):
        self._quantity = int(value)

    def is_available(self) -> bool:
        return self._quantity > 0

    def borrow_one(self) -> bool:
        if self._quantity > 0:
            self._quantity -= 1
            return True
        return False

    def return_one(self):
        self._quantity += 1

    @abstractmethod
    def loan_info(self) -> str:

        raise NotImplementedError

    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Item":
        raise NotImplementedError

    def __str__(self):
        return f"[{self._id}] {self._title} ({self._publication_year}) - Cant: {self._quantity}"


class Book(Item):
    """
    Clase Book que hereda de Item. Añade atributos específicos como author y genre.
    """
    def __init__(self, item_id: int, title: str, author: str, publication_year: int, genre: str, quantity: int):
        super().__init__(item_id, title, publication_year, quantity)
        self._author = str(author)
        self._genre = str(genre)

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, value: str):
        self._author = str(value)

    @property
    def genre(self) -> str:
        return self._genre

    @genre.setter
    def genre(self, value: str):
        self._genre = str(value)

    def loan_info(self) -> str:
        # Polimorfismo: los libros pueden prestarse por ejemplo 21 días
        return "Libro — plazo de préstamo: 21 días"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "type": "book",
            "id": self._id,
            "title": self._title,
            "author": self._author,
            "publication_year": self._publication_year,
            "genre": self._genre,
            "quantity": self._quantity
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Book":
        return cls(
            item_id=data["id"],
            title=data["title"],
            author=data.get("author", ""),
            publication_year=data.get("publication_year", 0),
            genre=data.get("genre", "Other"),
            quantity=data.get("quantity", 0)
        )

    def __str__(self):
        return f"Libro {super().__str__()} — Autor: {self._author} — Género: {self._genre}"


class Magazine(Item):
    """
    Clase Magazine (Revista) que hereda de Item. Añade número y periodicidad.
    """
    def __init__(self, item_id: int, title: str, issue: str, publication_year: int, periodicity: str, quantity: int):
        super().__init__(item_id, title, publication_year, quantity)
        self._issue = str(issue)
        self._periodicity = str(periodicity)

    @property
    def issue(self) -> str:
        return self._issue

    @issue.setter
    def issue(self, value: str):
        self._issue = str(value)

    @property
    def periodicity(self) -> str:
        return self._periodicity

    @periodicity.setter
    def periodicity(self, value: str):
        self._periodicity = str(value)

    def loan_info(self) -> str:
        # Polimorfismo: revistas tal vez préstamo más corto
        return "Revista — plazo de préstamo: 7 días"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "type": "magazine",
            "id": self._id,
            "title": self._title,
            "issue": self._issue,
            "publication_year": self._publication_year,
            "periodicity": self._periodicity,
            "quantity": self._quantity
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Magazine":
        return cls(
            item_id=data["id"],
            title=data["title"],
            issue=data.get("issue", ""),
            publication_year=data.get("publication_year", 0),
            periodicity=data.get("periodicity", ""),
            quantity=data.get("quantity", 0)
        )

    def __str__(self):
        return f"Revista {super().__str__()} — Nº: {self._issue} — Periodicidad: {self._periodicity}"


class User:
    """
    Clase Usuario: guarda los datos del miembro y la lista de ítems prestados (IDs).
    Encapsula atributos con properties.
    """
    def __init__(self, user_id: int, name: str):
        self._id = int(user_id)
        self._name = str(name)
        self._borrowed: List[int] = []  # lista de item IDs prestados

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = str(value)

    @property
    def borrowed(self) -> List[int]:
        # devolvemos copia para no exponer la lista interna a modificación directa
        return list(self._borrowed)

    def borrow_item(self, item_id: int) -> None:
        self._borrowed.append(int(item_id))

    def return_item(self, item_id: int) -> bool:
        try:
            self._borrowed.remove(int(item_id))
            return True
        except ValueError:
            return False

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self._id,
            "name": self._name,
            "borrowed": list(self._borrowed)
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "User":
        u = cls(user_id=data["id"], name=data.get("name", ""))
        for it in data.get("borrowed", []):
            u.borrow_item(int(it))
        return u

    def __str__(self):
        return f"[{self._id}] {self._name} — Prestados: {len(self._borrowed)}"


# -------------------------
# CLASE LIBRERÍA (AGGREGATOR)
# -------------------------

class Library:

    def __init__(self, items_file: str = "items.json", users_file: str = "users.json"):
        self._items: Dict[int, Item] = {}     # mapa id -> Item
        self._users: Dict[int, User] = {}     # mapa id -> User
        self._items_file = items_file
        self._users_file = users_file
        self._next_item_id = 1
        self._next_user_id = 1

        # Al inicializar, intentamos cargar archivos si existen
        self.load()

    # --- Generación de IDs (simples auto-incrementales)
    def _gen_item_id(self) -> int:
        while self._next_item_id in self._items:
            self._next_item_id += 1
        nid = self._next_item_id
        self._next_item_id += 1
        return nid

    def _gen_user_id(self) -> int:
        while self._next_user_id in self._users:
            self._next_user_id += 1
        nid = self._next_user_id
        self._next_user_id += 1
        return nid

    # --- Registro de usuarios e ítems
    def register_user(self, name: str, user_id: Optional[int] = None) -> User:
        uid = int(user_id) if user_id is not None else self._gen_user_id()
        if uid in self._users:
            raise ValueError(f"Usuario con ID {uid} ya existe.")
        user = User(user_id=uid, name=name)
        self._users[uid] = user
        return user

    def register_book(self, title: str, author: str, publication_year: int, genre: str, quantity: int, item_id: Optional[int] = None) -> Book:
        iid = int(item_id) if item_id is not None else self._gen_item_id()
        if iid in self._items:
            raise ValueError(f"Item con ID {iid} ya existe.")
        book = Book(item_id=iid, title=title, author=author, publication_year=publication_year, genre=genre, quantity=quantity)
        self._items[iid] = book
        return book

    def register_magazine(self, title: str, issue: str, publication_year: int, periodicity: str, quantity: int, item_id: Optional[int] = None) -> Magazine:
        iid = int(item_id) if item_id is not None else self._gen_item_id()
        if iid in self._items:
            raise ValueError(f"Item con ID {iid} ya existe.")
        mag = Magazine(item_id=iid, title=title, issue=issue, publication_year=publication_year, periodicity=periodicity, quantity=quantity)
        self._items[iid] = mag
        return mag

    # --- Búsquedas
    def find_item_by_id(self, item_id: int) -> Optional[Item]:
        return self._items.get(int(item_id))

    def find_user_by_id(self, user_id: int) -> Optional[User]:
        return self._users.get(int(user_id))

    def search_items(self, query: str) -> List[Item]:
        q = query.strip().lower()
        results: List[Item] = []
        for item in self._items.values():
            if q in item.title.lower():
                results.append(item)
                continue
            # si es Book, buscar por autor también
            if isinstance(item, Book) and q in item.author.lower():
                results.append(item)
        return results

    def search_users(self, query: str) -> List[User]:
        q = query.strip().lower()
        return [u for u in self._users.values() if q in u.name.lower()]

    # --- Préstamos y devoluciones
    def loan_item(self, user_id: int, item_id: int) -> bool:
        user = self.find_user_by_id(user_id)
        item = self.find_item_by_id(item_id)
        if user is None:
            print(f"Usuario con ID {user_id} no encontrado.")
            return False
        if item is None:
            print(f"Ítem con ID {item_id} no encontrado.")
            return False
        if not item.is_available():
            print("Ítem no disponible para préstamo.")
            return False
        success = item.borrow_one()
        if success:
            user.borrow_item(item_id)
            print(f"Préstamo realizado: {user.name} -> {item.title}")
            print(item.loan_info())  # comportamiento polimórfico: info del préstamo según tipo
            return True
        else:
            print("No se pudo realizar el préstamo.")
            return False

    def return_item(self, user_id: int, item_id: int) -> bool:
        user = self.find_user_by_id(user_id)
        item = self.find_item_by_id(item_id)
        if user is None:
            print(f"Usuario con ID {user_id} no encontrado.")
            return False
        if item is None:
            print(f"Ítem con ID {item_id} no encontrado.")
            return False
        returned = user.return_item(item_id)
        if returned:
            item.return_one()
            print(f"Devolución procesada: {user.name} devolvió {item.title}")
            return True
        else:
            print("El usuario no tiene registrado ese ítem como prestado.")
            return False

    # --- Visualización
    def list_items(self) -> List[Item]:
        return list(self._items.values())

    def list_users(self) -> List[User]:
        return list(self._users.values())

    # --- Persistencia (JSON)
    def save(self) -> None:
        items_serialized = [item.to_dict() for item in self._items.values()]
        users_serialized = [user.to_dict() for user in self._users.values()]
        try:
            with open(self._items_file, "w", encoding="utf-8") as f:
                json.dump(items_serialized, f, indent=2, ensure_ascii=False)
            with open(self._users_file, "w", encoding="utf-8") as f:
                json.dump(users_serialized, f, indent=2, ensure_ascii=False)
            print("Datos guardados correctamente.")
        except Exception as e:
            print("Error al guardar archivos:", e)

    def load(self) -> None:
        # Cargamos items
        if os.path.exists(self._items_file):
            try:
                with open(self._items_file, "r", encoding="utf-8") as f:
                    items_data = json.load(f)
                for d in items_data:
                    typ = d.get("type", "").lower()
                    if typ == "book":
                        item = Book.from_dict(d)
                    elif typ == "magazine":
                        item = Magazine.from_dict(d)
                    else:
                        # Si se añaden más tipos en el futuro, se puede extender aquí.
                        continue
                    self._items[item.id] = item
                    # asegurar que next_item_id esté por encima
                    if item.id >= self._next_item_id:
                        self._next_item_id = item.id + 1
            except Exception as e:
                print("Error al cargar items:", e)

        # Cargamos usuarios
        if os.path.exists(self._users_file):
            try:
                with open(self._users_file, "r", encoding="utf-8") as f:
                    users_data = json.load(f)
                for d in users_data:
                    user = User.from_dict(d)
                    self._users[user.id] = user
                    if user.id >= self._next_user_id:
                        self._next_user_id = user.id + 1
            except Exception as e:
                print("Error al cargar usuarios:", e)

    # --- Helpers de utilidad
    def ensure_save_files_exist(self) -> None:
        if not os.path.exists(self._items_file):
            with open(self._items_file, "w", encoding="utf-8") as f:
                json.dump([], f)
        if not os.path.exists(self._users_file):
            with open(self._users_file, "w", encoding="utf-8") as f:
                json.dump([], f)


# -------------------------
# INTERFAZ DE CONSOLA (MENU)
# -------------------------

def clear_screen():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception:
        pass


def prompt_int(msg: str, allow_empty: bool = False, default: Optional[int] = None) -> Optional[int]:
    while True:
        s = input(msg).strip()
        if s == "" and allow_empty:
            return default
        try:
            return int(s)
        except ValueError:
            print("Por favor ingresa un número entero válido.")


def menu_register_item(lib: Library):
    print("\n--- Registrar ítem ---")
    print("1) Libro")
    print("2) Revista")
    choice = input("Tipo (1/2): ").strip()
    if choice == "1":
        title = input("Título: ").strip()
        author = input("Autor: ").strip()
        year = prompt_int("Año de publicación: ")
        genre = input("Género: ").strip()
        qty = prompt_int("Cantidad: ")
        book = lib.register_book(title=title, author=author, publication_year=year, genre=genre, quantity=qty)
        print(f"Libro registrado: {book}")
    elif choice == "2":
        title = input("Título: ").strip()
        issue = input("Número/Edición: ").strip()
        year = prompt_int("Año de publicación: ")
        periodicity = input("Periodicidad (mensual, semanal...): ").strip()
        qty = prompt_int("Cantidad: ")
        mag = lib.register_magazine(title=title, issue=issue, publication_year=year, periodicity=periodicity, quantity=qty)
        print(f"Revista registrada: {mag}")
    else:
        print("Opción inválida.")


def menu_register_user(lib: Library):
    print("\n--- Registrar usuario ---")
    name = input("Nombre: ").strip()
    user = lib.register_user(name=name)
    print(f"Usuario creado: {user}")


def menu_list_items(lib: Library):
    print("\n--- Ítems en la biblioteca ---")
    items = lib.list_items()
    if not items:
        print("No hay ítems registrados.")
    else:
        for item in items:
            print(item)


def menu_list_users(lib: Library):
    print("\n--- Usuarios registrados ---")
    users = lib.list_users()
    if not users:
        print("No hay usuarios registrados.")
    else:
        for user in users:
            print(user)


def menu_search(lib: Library):
    print("\n--- Búsqueda ---")
    tipo = input("Buscar (1) Ítems (2) Usuarios: ").strip()
    q = input("Término de búsqueda: ").strip()
    if tipo == "1":
        res = lib.search_items(q)
        if not res:
            print("No se encontraron ítems.")
        else:
            for it in res:
                print(it)
    elif tipo == "2":
        res = lib.search_users(q)
        if not res:
            print("No se encontraron usuarios.")
        else:
            for u in res:
                print(u)
    else:
        print("Opción inválida.")


def menu_loan(lib: Library):
    print("\n--- Prestar ítem ---")
    user_id = prompt_int("ID de usuario: ")
    item_id = prompt_int("ID de ítem: ")
    if user_id is None or item_id is None:
        print("IDs inválidos.")
        return
    lib.loan_item(user_id=user_id, item_id=item_id)


def menu_return(lib: Library):
    print("\n--- Devolver ítem ---")
    user_id = prompt_int("ID de usuario: ")
    item_id = prompt_int("ID de ítem: ")
    if user_id is None or item_id is None:
        print("IDs inválidos.")
        return
    lib.return_item(user_id=user_id, item_id=item_id)


def menu_save_load(lib: Library):
    print("\n--- Guardar / Cargar datos ---")
    print("1) Guardar ahora")
    print("2) Cargar desde archivos (sobre-escribirá estado actual en memoria)")
    opt = input("Opción: ").strip()
    if opt == "1":
        lib.save()
    elif opt == "2":
        confirm = input("¿Seguro? Esto sobrescribirá los cambios no guardados. (s/N): ").strip().lower()
        if confirm == 's':
            lib.load()
            print("Datos cargados.")
        else:
            print("Operación cancelada.")
    else:
        print("Opción inválida.")


def main_menu():
    lib = Library()
    lib.ensure_save_files_exist()

    while True:
        print("\n=== Sistema de Manejo de Biblioteca ===")
        print("1) Registrar ítem (Libro/Revista)")
        print("2) Registrar usuario")
        print("3) Prestar ítem")
        print("4) Devolver ítem")
        print("5) Buscar ítems/usuarios")
        print("6) Mostrar ítems")
        print("7) Mostrar usuarios")
        print("8) Guardar datos")
        print("9) Cargar datos")
        print("0) Salir")
        opt = input("Selecciona una opción: ").strip()
        if opt == "1":
            menu_register_item(lib)
        elif opt == "2":
            menu_register_user(lib)
        elif opt == "3":
            menu_loan(lib)
        elif opt == "4":
            menu_return(lib)
        elif opt == "5":
            menu_search(lib)
        elif opt == "6":
            menu_list_items(lib)
        elif opt == "7":
            menu_list_users(lib)
        elif opt == "8":
            lib.save()
        elif opt == "9":
            confirm = input("¿Cargar desde archivos y sobrescribir estado actual? (s/N): ").strip().lower()
            if confirm == 's':
                lib.load()
                print("Datos cargados desde archivos.")
            else:
                print("Operación cancelada.")
        elif opt == "0":
            print("Guardando datos antes de salir...")
            lib.save()
            print("Saliendo. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main_menu()