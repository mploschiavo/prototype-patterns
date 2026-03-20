FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src
COPY src/HelloWorldService/HelloWorldService.csproj src/HelloWorldService/
RUN dotnet restore src/HelloWorldService/HelloWorldService.csproj
COPY src/HelloWorldService src/HelloWorldService
RUN dotnet publish src/HelloWorldService/HelloWorldService.csproj -c Release -o /app/publish /p:UseAppHost=false

FROM mcr.microsoft.com/dotnet/aspnet:8.0
WORKDIR /app
COPY --from=build /app/publish .
ENV ASPNETCORE_URLS=http://+:8080
EXPOSE 8080
ENTRYPOINT ["dotnet", "HelloWorldService.dll"]
