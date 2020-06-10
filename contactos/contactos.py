#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 11:16:17 2020

@author: daniel
"""
import time
import csv
class Contact:
    def __init__(self, name, phone, email):
        self._name = name
        self._phone = phone
        self._email = email
class ContactBook:
    
           
    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()

    def _print_contact(self, contact):

        print('--- * --- * --- * --- * --- * --- * --- * ---')
        print('Nombre: {}'.format(contact._name))
        print('Teléfono: {}'.format(contact._phone))
        print('Email: {}'.format(contact._email))
        print('--- * --- * --- * --- * --- * --- * --- * ---')

    def display(self):
        for contact in self._contacts:
            self._print_contact(contact)
    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact._name.lower() == name.lower():
                del self._contacts[idx]
                break
            self._save()    
    def search(self, name):
        for contact in self._contacts:
            if contact._name.lower() == name.lower():
                print(self._print_contact(contact))
                break
        else:
            self._not_found()

    def _not_found(self):
        print('')
        print('**********************')
        print('CONTACTO NO ENCONTRADO')
        print('**********************')
        
    def update(self, name, phone, email):
        for contact in self._contacts:
    
            if contact._name.lower() == name.lower():
                contact._name = name
                contact._phone = phone
                contact._email = email
                print('contacto actualizad0')
                break
        else:
            self._not_found()
            
    def _save(self):
        with open('contactos.csv','w') as f:
            writer = csv.writer(f)
            writer.writerow(('nombre','telefono','correo'))
            
            for contact in self._contacts:
                writer.writerow((contact._name, contact._phone, contact._email))
      
                

def run():
    contact_book = ContactBook()
    
    with open('contactos.csv', 'r') as f:
        reader = csv.reader(f)
        
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            contact_book.add(row[0], row[1],row[2])
        
    while True:
        menu = input('''
                       [a]ñadir contacto
                       [ac]tualizar contacto
                       [b]uscar contacto
                       [e]liminar contacto
                       [l]istar contacto
                       [s]alir

                     ''')
        if menu == 'a':
            name = input('Nombre: ')
            phone = input('Número de telefono: ')
            email = input('Correo: ')
            time.sleep(3)
            contact_book.add(name, phone, email)
        elif menu == 'ac':
            name = input('Nombre: ')
            phone = input('Número de telefono: ')
            email = input('Correo: ')
            time.sleep(3)
            contact_book.update(name, phone, email)
        elif menu == 'b':
            name = input('nombre: ')
            print('searching...')
            time.sleep(3)
            contact_book.search(name)
        elif menu == 'e':
            name = input('nombre: ')
            contact_book.delete(name)
        elif menu == 'l':
            contact_book.display()
        else:
            break



if __name__ == '__main__':
    print('C O N T A C T O S')
    run()
    