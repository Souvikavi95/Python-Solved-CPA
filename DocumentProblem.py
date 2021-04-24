class Document:
    def __init__(self, docId, docName, docDetails):
        self.docId = docId
        self.docName = docName
        self.docDetails = docDetails


class DocumentArchive:
    def __init__(self, archiveId, documentList):
        self.archiveId = archiveId
        self.documentList = documentList

    def findDateFromDocumentDetails(self):
        result = []
        for doc in self.documentList:
            item_list = (doc.docDetails.split(","))
            for i in range(len(item_list)):
                item_list[i] = item_list[i].strip()

            for part in item_list:
                if part.count("/") == 2:
                    result.append((doc.docId, part))
        return result

    def countDocumentsOfGivenType(self, docType):
        count = 0
        for doc in self.documentList:
            temp = doc.docName.split(".")
            if temp[1].lower() == docType.lower():
                count += 1
        return count


if __name__ == "__main__":
    no_of_docs = int(input())
    document_list =[]
    for i in range(no_of_docs):
        a = int(input())
        b = input()
        c = input()
        document_list.append(Document(a,b,c))

    obj = DocumentArchive(100, document_list)
    doc_type = input()
    ans1 = obj.findDateFromDocumentDetails()
    if (len(ans1)) > 0:
        for k in ans1:
            print(k[0], end =" ")
            print(k[1])
    ans2 = obj.countDocumentsOfGivenType(doc_type)
    print("Document count = " + str(ans2))
